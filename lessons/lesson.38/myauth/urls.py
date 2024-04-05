from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

app_name = 'myauth'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path(
        'register/',
        views.MyUserCreateView.as_view(),
        name='register',
    ),
]
