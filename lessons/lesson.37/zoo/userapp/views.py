from django.views.generic import CreateView
from .models import MyUser
from .forms import RegisterForm
from django.contrib.auth.views import LoginView as LoginViewContrib , LogoutView as LogoutViewContrib


class RegisterView(CreateView):
    model = MyUser
    form_class = RegisterForm
    template_name = 'userapp/register.html'
    success_url = '/login/'


class LoginView(LoginViewContrib):
    template_name = 'userapp/login.html'

    # self.request.user


class LogoutView(LogoutViewContrib):
    pass