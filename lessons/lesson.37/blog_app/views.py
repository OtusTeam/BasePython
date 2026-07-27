from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Главная страница."""
    return HttpResponse("<h1>Hello, world.</h1><hr>You're the blog app!")


def about(request):
    """Страница о нас."""
    return HttpResponse("<h2>Страница о нас.</h2><hr>You're the blog app!")