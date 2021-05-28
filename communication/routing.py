# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/communication/(?P<room_name>\w+)/(?P<username>\w+)/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/chat/(?P<user>\w+)/(?P<username>\w+)/$', consumers.PersonalConsumer.as_asgi()),
    
   

]

