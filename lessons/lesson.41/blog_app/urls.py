from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('add_post/', views.add_post, name='add_post'),
    path('posts/<int:post_id>/edit', views.edit_post, name='edit_post'),
    path('posts/<int:post_id>/delete', views.delete_post, name='delete_post'),
    path('authors/', views.author_list, name='author_list'),
    path('authors/<int:author_id>/', views.author_detail, name='author_detail'),
]
