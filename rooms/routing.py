from django.urls import path

from . import clients

websocket_urlpatterns = [
    path('ws/<str:room_name>/', clients.ChatClient.as_asgi()),
]
