from django.shortcuts import render
from .models import MyUser
from django.views.generic import CreateView
from .forms import MyUserCreationForm
from django.contrib.auth.views import LoginView, LogoutView


class UserCreateView(CreateView):
    model = MyUser
    template_name = 'users/create.html'
    success_url = '/'
    # fields = '__all__'
    form_class = MyUserCreationForm


class AuthView(LoginView):
    template_name = 'users/login.html'
    success_url = '/'


class MyUserLogoutView(LogoutView):
    pass
