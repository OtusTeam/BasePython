from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.AboutTemplateView.as_view(), name='about'),
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/add/', views.PostCreateView.as_view(), name='add_post'),
    path('posts/<int:pk>/edit', views.PostUpdateView.as_view(), name='edit_post'),
    path('posts/<int:pk>/delete', views.PostDeleteView.as_view(), name='delete_post'),
    path('authors/', views.author_list, name='author_list'),
    path('authors/<int:author_id>/', views.author_detail, name='author_detail'),
]
