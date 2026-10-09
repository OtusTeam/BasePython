from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello, world.</h1> <hr> <p>You're at the blog</p>")


def about(request):
    return HttpResponse("<h1>About us.</h1> <hr> <p>Информация о нас</p>")