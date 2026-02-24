from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from blog_app.models import Post, Author


def index(request):
    """Главная страница."""
    return render(request, "blog_app/index.html")


def about(request):
    """Главная страница."""
    return HttpResponse("<h2>Cтраница о нас.</h2>")


def post_list(request):
    """Список постов."""
    posts = Post.objects.all()
    context = {
        'title': 'Список постов!',
        'posts': posts,
    }
    return render(request, "blog_app/post_list.html", context=context)


def post_detail(request, post_id):
    """Детайльный пост."""
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post,
    }

    return render(request, "blog_app/post_detail.html", context=context)


def author_list(request):
    """Список авторов."""
    authors = Author.objects.all()
    context = {
        'title': 'Список Авторов!',
        'authors': authors,
    }
    return render(request, "blog_app/author_list.html", context=context)


def author_detail(request, author_id):
    """Детальный автор."""
    author = get_object_or_404(Author, pk=author_id)
    context = {
        'author': author,
    }

    return render(request, "blog_app/author_detail.html", context=context)