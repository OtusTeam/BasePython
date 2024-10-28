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
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]
