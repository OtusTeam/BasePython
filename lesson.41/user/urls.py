from django.urls import path
from .views import create_user_view, RegistrationView
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('create_user/', create_user_view, name='create_user'),
    path('registr/', RegistrationView.as_view(), name='registr'),
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', LoginView.as_view(), name='logout'),
]
