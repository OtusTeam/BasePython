from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from blog_app.models import Post


def index(request):
    """Главная страница."""
    return render(request, 'blog_app/index.html')


def about(request):
    """Страница о нас."""
    return HttpResponse("<h2>Страница о нас.</h2><hr>You're the blog app!")


def post_list(request):
    """Список постов."""
    posts1 = Post.objects.all()
    context = {
        'posts': posts1,
        'title': 'Список постов!'
    }
    return render(request, 'blog_app/post_list.html', context=context)


def post_detail(request, post_id):
    """Детальный постов."""
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post,
        'title': post.title,
    }
    return render(request, 'blog_app/post_detail.html', context=context)