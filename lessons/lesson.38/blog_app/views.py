from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Author


def index(request):
    """Главная страница."""
    return render(request, 'blog_app/index.html')


def about(request):
    """Страница о нас."""
    return HttpResponse('<h1>About us</h1>')


def post_list(request):
    """Cтраница всех постов."""
    posts = Post.objects.all()
    context = {
        'title': 'Список постов',
        'posts': posts,
    }
    return render(request, 'blog_app/post_list.html', context=context)


def post_detail(request, post_id):
    """Cтраница для одного поста."""
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post,
    }
    return render(request, 'blog_app/post_detail.html', context=context)


def author_list(request):
    """Cтраница всех авторов."""
    authors = Author.objects.all()
    context = {
        'title': 'Список авторов',
        'authors': authors,
    }
    return render(request, 'blog_app/author_list.html', context=context)