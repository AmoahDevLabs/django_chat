"""django_chat URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

from rooms.views import front_page

urlpatterns = [
    path('', include('users.urls')),
    path('rooms/', include('rooms.urls')),
    path('', front_page, name='font_page'),
    path('admin/', admin.site.urls),
]
