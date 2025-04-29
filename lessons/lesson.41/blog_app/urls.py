from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('posts/', views.post_list, name='posts'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('posts/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('add-post/', views.app_post, name='add_post'),
    path('authors/', views.author_list, name='authors'),
    path('authors/<int:author_id>/', views.author_posts, name='author_posts'),
]