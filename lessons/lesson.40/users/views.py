from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .models import MyUser
from .forms import RegisterForm


class RegisterView(CreateView):
    model = MyUser
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = '/'


class AuthView(LoginView):
    template_name = 'users/login.html'

