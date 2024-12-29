from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Shop Hello, world. You're at the blog index.")


def contacts(request):
    return HttpResponse("Shop Hello, contacts!!")