from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    """Главная страница."""
    return HttpResponse("<h1>Главная страница.</h1>")


def about(request):
    """Страница о нас."""
    return HttpResponse("<h2>Страница о нас</h2>")