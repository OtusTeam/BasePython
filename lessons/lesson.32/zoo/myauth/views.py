from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from myauth.forms import MyUserCreationForm
from myauth.models import MyUser


class MyLoginView(LoginView):
    pass


class MyLogoutView(LogoutView):
    pass


class UserCreateView(CreateView):
    model = MyUser
    success_url = reverse_lazy('main_page')
    form_class = MyUserCreationForm
