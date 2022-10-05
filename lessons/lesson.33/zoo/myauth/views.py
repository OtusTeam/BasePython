from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.views import (
    LoginView as LoginViewGeneric,
    LogoutView as LogoutViewGeneric,
)
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy

from .forms import AuthenticationForm, UserCreationForm
from .models import UserModel



@login_required
# @permission_required(["perm1", "perm2", ...])
def secret_view(request):
    return HttpResponse("secret info: ...")


class MeView(TemplateView):
    template_name = "myauth/me.html"


class UserCreationView(CreateView):
    model = UserModel
    form_class = UserCreationForm
    success_url = reverse_lazy("myauth:me")
    template_name = "registration/register.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password2"]
        user = authenticate(self.request, username=username, password=password)
        login(self.request, user=user)
        return response


class LoginView(LoginViewGeneric):
    form_class = AuthenticationForm
    next_page = reverse_lazy("myauth:me")


class LogoutView(LogoutViewGeneric):
    next_page = reverse_lazy("myauth:me")
