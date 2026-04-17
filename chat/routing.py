from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    # Updated to [\w-]+ to support slugs with hyphens
    re_path(r'ws/chat/(?P<room_name>[\w-]+)/$', consumers.ChatConsumer.as_asgi()),
]