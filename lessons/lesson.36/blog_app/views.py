from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>BLOG !!! Hello, world. You're at the polls index!!!</h1>")


def about(request):
    return HttpResponse("<h1>About me info</h1>")