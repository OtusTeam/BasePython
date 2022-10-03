from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.views import (
    LoginView as LoginViewGeneric,
    LogoutView as LogoutViewGeneric,
)
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.urls import reverse_lazy

from .forms import AuthenticationForm


@login_required
# @permission_required(["perm1", "perm2", ...])
def secret_view(request):
    return HttpResponse("secret info: ...")


class MeView(TemplateView):
    template_name = "myauth/me.html"


class LoginView(LoginViewGeneric):
    form_class = AuthenticationForm
    next_page = reverse_lazy("myauth:me")


class LogoutView(LogoutViewGeneric):
    next_page = reverse_lazy("myauth:me")
