from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Author

# Create your views here.
def index(request):
    return render(request, 'blog_app/home.html')


def contacts(request):
    return HttpResponse("Hello, contacts!!")


def post_list(request):
    posts = Post.objects.all()
    context = {
        'title': 'Список постов',
        'posts': posts
    }
    return render(request, 'blog_app/post_list.html', context=context)


def post_detail(request, post_id):
    # post = Post.objects.get(pk=post_id)
    post =  get_object_or_404(Post, pk=post_id)

    context = {
        'title': post.title,
        'post': post
    }
    return render(request, 'blog_app/post_detail.html', context=context)


def author_list(request):
    authors = Author.objects.all()
    context = {
        'title': 'Список авторов',
        'authors': authors
    }
    return render(request, 'blog_app/author_list.html', context=context)