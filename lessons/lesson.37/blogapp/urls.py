from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.index, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('author_create/', views.author_create, name='author_create'),
    path('authors/', views.authors, name='authors'),
]
