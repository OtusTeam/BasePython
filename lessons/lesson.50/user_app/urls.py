from django.urls import path
from user_app.views import RegisterView, CustomLogoutView, CustomLoginView


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout", CustomLogoutView.as_view(), name="logout"),
]
