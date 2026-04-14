import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        user = self.scope["user"]
        if user.is_authenticated:
            self.accept()
            self.send(text_data=json.dumps({
                'message': f'SUCCESS: Welcome to the secure socket, {user.username}!'
            }))
        else:
            self.close()