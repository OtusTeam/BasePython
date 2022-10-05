from django.urls import path

from .views import (
    secret_view,
    MeView,
    LoginView,
    LogoutView,
    UserCreationView,
)

app_name = "myauth"

urlpatterns = [
    path("secret/", secret_view, name="secret"),
    path("me/", MeView.as_view(), name="me"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", UserCreationView.as_view(), name="register"),
]
