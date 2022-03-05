from django.urls import path
from .views import room_list, room_detail

urlpatterns = [
    path('', room_list, name='rooms'),
    path('<slug:slug>/', room_detail, name='room'),
]
