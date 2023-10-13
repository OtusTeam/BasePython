from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

import myauth.views as myauth

app_name = 'myauth'

urlpatterns = [
    path('register/', myauth.MyUserCreateView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
