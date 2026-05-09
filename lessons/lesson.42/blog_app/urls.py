from django.urls import path
from blog_app.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, AboutTemplateView, IndexTemplateView


urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/add/', PostCreateView.as_view(), name='post_add'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

]
