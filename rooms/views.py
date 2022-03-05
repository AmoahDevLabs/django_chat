from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from rooms.models import Room, Message


def front_page(request):
    return render(request, 'rooms/font_page.html')


@login_required
def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'rooms/rooms.html', {'rooms': rooms})


@login_required
def room_detail(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[:15]
    return render(request, 'rooms/room.html', {'room': room,
                                               'messages': messages})
