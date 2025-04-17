from django.shortcuts import render
from .models import Post
from random import randint
from django.http import HttpResponse
# Create your views here.


def index(request):
    post = Post(title=f'Post {randint(1, 100)}', content=f'Hello world {randint(1, 100)}', author=f'Admin{randint(1, 100)}')
    post = Post(title=f'Post {randint(1, 100)}', content=f'Hello world {randint(1, 100)}', author=f'Admin{randint(1, 100)}')
    post.save()
    return HttpResponse("""
    <h1>Hello, world.</h1> 
    <p>You're at the blog index.</p>""")


def about(request):
    return HttpResponse("""
    <h1>О нас.</h1> 
    <p>Блог ОТУС.</p>""")