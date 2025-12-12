from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    """Главная страница."""
    return HttpResponse('<h1>Привет, ОТУС! </h1>')


def about(request):
    """Страница о нас."""
    return HttpResponse('<h1>О нас! </h1>')