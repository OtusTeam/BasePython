from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView, DetailView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView


# Create your views here.
# 1. Регистрация - создание пользователя
from users.forms import RegistrationForm


class RegistrationView(CreateView):
    model = User
    # fields = ('username', 'email', 'password')
    form_class = RegistrationForm
    success_url = '/'
    template_name = 'users/user_form.html'


class UserLoginView(LoginView):
    template_name = 'users/login_form.html'


class UserLogoutView(LogoutView):
    pass


class UserDetailView(DetailView):
    model = User
    template_name = 'users/user_detail.html'

    def get_queryset(self):
        return super().get_queryset().filter(id=self.request.user.id)


class UserTemplateView(TemplateView):
    template_name = 'users/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.select_related("profile").filter(pk=self.request.user.pk).first()
        context['object'] = user
        # print(user)
        # print(repr(user))
        # print(repr(user.profile))
        return context
