from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Hello, OTUS!!!</h1>')


def about(request):
    return HttpResponse('<h2>ABOUT US</h2>')