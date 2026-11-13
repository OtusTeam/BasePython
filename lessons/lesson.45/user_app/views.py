from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.views.generic import FormView, RedirectView
from django.urls import reverse_lazy


from .forms import CustomAuthenticationForm, CustomUserCreationForm


class RegistrationView(FormView):
    form_class = CustomUserCreationForm
    template_name = 'user_app/registration.html'
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
        """Можно определять, куда перенаправить пользователя после успешной аутентификации."""
        return self.success_url


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')