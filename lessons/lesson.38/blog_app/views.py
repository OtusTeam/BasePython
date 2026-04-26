from django.shortcuts import render, get_object_or_404
from blog_app.models import Post


def index(request):
    """Главная страница."""
    return render(request, 'blog_app/index.html')


def about(request):
    """Страница о нас."""
    return render(request, 'blog_app/about.html')


def post_list(request):
    """Список постов."""
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog_app/post_list.html', context=context)


def post_detail(request, post_id):
    """Детальный пост."""
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post
    }
    return render(request, 'blog_app/post_detail.html', context=context)