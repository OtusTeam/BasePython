from django.urls import path, include
from django.contrib.auth.views import LogoutView

from .views import UserCreationView, LoginView


urlpatterns = [
    path('myauth/register/', UserCreationView.as_view(), name="user-profile"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]
