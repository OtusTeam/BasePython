from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexTemplateView.as_view(), name='index'),
    path('about/', views.about, name='about'),
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('posts/add/', views.PostCreateView.as_view(), name='add_post'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='edit_post'),
    path('authors/', views.author_list, name='author_list'),

    # path('', views.index, name='index'),
    # path('posts/', views.post_list, name='post_list'),
    # path('posts/add/', views.add_post, name='add_post'),
    # path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    # path('posts/<int:post_id>/edit/', views.edit_post, name='edit_post'),
]
