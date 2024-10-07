from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.index),
    path('contacts/', views.contacts),
]
