from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, RedirectView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from .forms import CustomUserCreationForm, CustomAuthenticationForm


class RegisterView(FormView):
    form_class = CustomUserCreationForm
    template_name = 'user_app/register.html'
    success_url = reverse_lazy('login')

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
    next_page = reverse_lazy('post_list')
