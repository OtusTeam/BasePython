from django.urls import path
from blog_app.views import index, about
from blog_app.views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)


urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("posts/", PostListView.as_view(), name="post_list"),
    path("posts/add/", PostCreateView.as_view(), name="add_post"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="edit_post"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="delete_post"),
]
