from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('contacts/', views.contacts, name='contacts'),
    # path('posts/', views.post_list, name='post_list'),
    path('posts/', views.PostListView.as_view(), name='post_list'),
    # path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('authors/', views.author_list, name='author_list'),
    path('add_post/', views.add_post, name='add_post'),
    # path('add_post_model/', views.add_post_model, name='add_post_model'),
    path('add_post_model/', views.PostCreateView.as_view(), name='add_post_model'),
    # path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('edit_post/<int:pk>/', views.PostUpdateView.as_view(), name='edit_post'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete_post'),
]
