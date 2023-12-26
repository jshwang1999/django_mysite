# chat_app/routing.py
from django.urls import re_path
from . import participants

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', participants.ChatParticipant.as_asgi()),
]