from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, RedirectView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from .forms import CustomAuthenticationForm, CustomUserCreationForm


class RegisterView(FormView):
    template_name = 'user_app/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class CustomLoginView(LoginView):
    template_name = 'user_app/login.html'
    authentication_form = CustomAuthenticationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('post_list')

    def get_success_url(self):
        return self.success_url


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('about')