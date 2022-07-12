from django.contrib.auth.views import LoginView as LoginViewGeneric
from django.urls import reverse_lazy

from django.views.generic import CreateView

from .forms import UserCreationForm
from .models import UserModel


class UserCreationView(CreateView):
    model = UserModel
    success_url = reverse_lazy("animals:list")
    form_class = UserCreationForm
    template_name = "registration/user_register.html"


class LoginView(LoginViewGeneric):
    next_page = reverse_lazy("animals:list")
