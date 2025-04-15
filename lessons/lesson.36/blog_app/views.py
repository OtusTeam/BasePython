from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("""
    <h1>Hello, world.</h1> 
    <p>You're at the blog index.</p>""")


def about(request):
    return HttpResponse("""
    <h1>О нас.</h1> 
    <p>Блог ОТУС.</p>""")