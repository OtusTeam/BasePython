from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('about/', views.about, name='about'),
    # path('posts/', views.post_list, name='posts'),
    # path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    # path('add-post/', views.add_post, name='add_post'),
    # path('posts/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('posts/', views.PostListView.as_view(), name='posts'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='edit_post'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete_post'),
    path('posts/add/', views.PostCreateView.as_view(), name='add_post'),
    path('authors/', views.author_list, name='authors'),
    path('authors/<int:author_id>/', views.author_posts, name='author_posts'),
]