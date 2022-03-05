from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.Login.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', views.RegisterView.as_view(), name='signup'),
]

hmtx_patterns = [
    path("check-username/", views.check_username, name='check-username'),
]

urlpatterns += hmtx_patterns