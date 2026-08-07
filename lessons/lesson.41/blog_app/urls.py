from django.urls import path
from blog_app.views import index, about, post_list, post_detail, post_add, post_edit


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('posts/', post_list, name='post_list'),
    path('posts/add/', post_add, name='post_add'),
    path('posts/<int:post_id>/', post_detail, name='post_detail'),
    path('posts/<int:post_id>/edit/', post_edit, name='post_edit'),
]
