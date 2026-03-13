from django.urls import path
from .views import about, author_list, author_detail #, post_delete
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, IndexTemplateView


urlpatterns = [
    # path('', index, name='index'),
    path('', IndexTemplateView.as_view(), name='index'),
    path('about/', about, name='about'),
    # path('posts/', post_list, name='post_list'),
    path('posts/', PostListView.as_view(), name='post_list'),
    # path('posts/add/', post_add, name='post_add'),
    path('posts/add/', PostCreateView.as_view() , name='post_add'),
    # path('posts/<int:post_id>/', post_detail, name='post_detail'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    # path('posts/<int:post_id>/edit/', post_edit, name='post_edit'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    # path('posts/<int:post_id>/delete/', post_delete, name='post_delete'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('authors/', author_list, name='author_list'),
    path('authors/<int:author_id>/', author_detail, name='author_detail'),
]
