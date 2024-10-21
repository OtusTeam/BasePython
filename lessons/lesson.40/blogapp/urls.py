from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.index, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('author_create/', views.author_create, name='author_create'),
    path('authors/', views.authors, name='authors'),
    path('author_form/', views.author_create_form, name='author_create_form'),
    path('author_update/<int:author_id>/', views.author_update_form, name='author_update_form'),
    path('author/<int:author_id>/', views.author, name='author'),
    path('post_detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post_list/', views.PostListView.as_view(), name='post_list'),
]
