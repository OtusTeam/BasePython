from django.urls import path
from blog_app.views import index, about, post_list, post_detail, add_post, edit_post


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('posts/', post_list, name='post_list'),
    path('posts/add/', add_post, name='add_post'),
    path('posts/<int:post_id>/', post_detail, name='post_detail'),
    path('posts/<int:post_id>/edit/', edit_post, name='edit_post'),
]
