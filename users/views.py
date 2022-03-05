from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from .forms import RegisterForm


class HomeView(TemplateView):
    template_name = 'home.html'


def next_route(request):
    if 'next' in request.POST:
        return redirect(request.POST.get('next'))
    else:
        return redirect('/')


class Login(LoginView):
    template_name = 'users/login.html'


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()  # save the user
        return super().form_valid(form)


def check_username(request):
    username = request.POST.get('username')
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("<div id='username-error' class='error'>This username already exists</div>")
    else:
        return HttpResponse("<div id='username-error' class='success'>This username is available</div>")