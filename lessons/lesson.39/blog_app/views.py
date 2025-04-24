from django.shortcuts import render, get_object_or_404
from .models import Post, Author
from random import randint
from django.http import HttpResponse
# Create your views here.


def index(request):
    # post = Post(title=f'Post {randint(1, 100)}', content=f'Hello world {randint(1, 100)}', author=f'Admin{randint(1, 100)}')
    # post = Post(title=f'Post {randint(1, 100)}', content=f'Hello world {randint(1, 100)}', author=f'Admin{randint(1, 100)}')
    # post.save()
    # return HttpResponse("""
    # <h1>Hello, world.</h1>
    # <p>You're at the blog index.</p>""")
    return render(request, 'blog_app/index.html')


def about(request):
    return HttpResponse("""
    <h1>О нас.</h1> 
    <p>Блог ОТУС.</p>""")


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog_app/post_list.html', context=context)


def post_detail(request, post_id):
    # post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, id=post_id)
    context = {
        'post': post
    }
    return render(request, 'blog_app/post_detail.html', context=context)


def author_list(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'blog_app/author_list.html', context=context)


def author_posts(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    posts = Post.objects.filter(author=author)
    context = {
        'author': author,
        'posts': posts
    }
    return render(request, 'blog_app/author_posts.html', context=context)