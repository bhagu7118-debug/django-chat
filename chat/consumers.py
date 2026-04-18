import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
from .models import Room, Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"
        self.user = self.scope["user"]

        # Join the room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
        # WELCOME LOGIC: Broadcast a join notification to the room
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': f'{self.user.username} has joined the room!',
                'username': 'System' 
            }
        )

        if self.user.is_authenticated:
            # 1. Tell everyone I joined (updates their "Online Users" list)
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'user_status',
                    'username': self.user.username,
                    'status': 'online'
                }
            )
            # 2. Ask others to identify themselves to populate my local list
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'user_list_request',
                    'requester': self.user.username
                }
            )

    async def disconnect(self, close_code):
        if self.user.is_authenticated:
            # Tell everyone I left
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'user_status',
                    'username': self.user.username,
                    'status': 'offline'
                }
            )
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        action_type = data.get('type', 'chat_message')

        # Handle sending a new message
        if action_type == 'chat_message':
            message = data['message']
            # Save to Database using helper method below
            msg_obj = await self.save_message(self.user.username, self.room_name, message)
            
            # Broadcast to everyone in the room
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'username': self.user.username,
                    'msg_id': msg_obj.id 
                }
            )
        
        # Handle editing an existing message (Advanced)
        elif action_type == 'edit_message':
            msg_id = data['msg_id']
            new_content = data['message']
            await self.update_message_db(msg_id, new_content)
            
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'message_edited',
                    'msg_id': msg_id,
                    'message': new_content
                }
            )

        # Response to a Roll Call (keeps the online list accurate)
        elif action_type == 'user_list_response':
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'user_status',
                    'username': self.user.username,
                    'status': 'online'
                }
            )

    # These methods send the events to the JavaScript "onmessage" function
    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))

    async def user_status(self, event):
        await self.send(text_data=json.dumps(event))

    async def message_edited(self, event):
        await self.send(text_data=json.dumps(event))

    async def user_list_request(self, event):
        await self.send(text_data=json.dumps(event))

    # Database helper methods
    @database_sync_to_async
    def save_message(self, username, room_slug, message):
        user = User.objects.get(username=username)
        room = Room.objects.get(slug=room_slug)
        return Message.objects.create(user=user, room=room, content=message)

    @database_sync_to_async
    def update_message_db(self, msg_id, content):
        # Ensures only the owner of the message can edit it
        Message.objects.filter(id=msg_id, user=self.user).update(content=content)