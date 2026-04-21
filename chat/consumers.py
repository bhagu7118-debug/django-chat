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

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

        # Notify others someone joined
        if self.user.is_authenticated:
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'user_status',
                    'username': self.user.username,
                    'status': 'online'
                }
            )
            # Request status from others already in the room
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'user_list_request',
                    'requester': self.user.username
                }
            )

    async def disconnect(self, close_code):
        if self.user.is_authenticated:
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
        action_type = data.get('type')

        if action_type == 'chat_message':
            message = data['message']
            msg_obj = await self.save_message(self.user.username, self.room_name, message)
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message_handler',
                    'message': message,
                    'username': self.user.username,
                    'msg_id': msg_obj.id 
                }
            )
        
        elif action_type == 'typing':
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'typing_handler',
                    'username': self.user.username,
                    'is_typing': data['is_typing']
                }
            )

        elif action_type == 'edit_message':
            await self.update_message_db(data['msg_id'], data['message'])
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'edit_handler',
                    'msg_id': data['msg_id'],
                    'message': data['message']
                }
            )

        elif action_type == 'delete_message':
            await self.delete_message_db(data['msg_id'])
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'delete_handler',
                    'msg_id': data['msg_id']
                }
            )

        elif action_type == 'user_list_response':
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'user_status',
                    'username': self.user.username,
                    'status': 'online'
                }
            )

    # --- CRITICAL: EVENT HANDLERS TO SEND DATA TO BROWSERS ---
    async def chat_message_handler(self, event):
        await self.send(text_data=json.dumps({
            'type': 'chat_message',
            'message': event['message'],
            'username': event['username'],
            'msg_id': event['msg_id']
        }))

    async def typing_handler(self, event):
        await self.send(text_data=json.dumps({
            'type': 'user_typing',
            'username': event['username'],
            'is_typing': event['is_typing']
        }))

    async def edit_handler(self, event):
        await self.send(text_data=json.dumps({
            'type': 'message_edited',
            'msg_id': event['msg_id'],
            'message': event['message']
        }))

    async def delete_handler(self, event):
        await self.send(text_data=json.dumps({
            'type': 'message_deleted',
            'msg_id': event['msg_id']
        }))

    async def user_status(self, event):
        await self.send(text_data=json.dumps(event))

    async def user_list_request(self, event):
        await self.send(text_data=json.dumps(event))

    # --- Database Methods ---
    @database_sync_to_async
    def save_message(self, username, room_slug, message):
        user = User.objects.get(username=username)
        room = Room.objects.get(slug=room_slug)
        return Message.objects.create(user=user, room=room, content=message)

    @database_sync_to_async
    def update_message_db(self, msg_id, content):
        Message.objects.filter(id=msg_id, user=self.user).update(content=content)

    @database_sync_to_async
    def delete_message_db(self, msg_id):
        Message.objects.filter(id=msg_id, user=self.user).delete()