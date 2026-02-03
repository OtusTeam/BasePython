from django.urls import path
from .views import RegistrationView, CustomLogoutView, CustomLoginView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),

]
