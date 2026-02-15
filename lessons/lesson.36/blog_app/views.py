from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Главная страница."""
    return HttpResponse("<h1>Главная страница.</h1>")


def about(request):
    """Главная страница."""
    return HttpResponse("<h2>Cтраница о нас.</h2>")