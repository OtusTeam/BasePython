from django.http import HttpResponse
from django.shortcuts import render

from blogapp.models import Author


# Create your views here.

# Семинар 1
# def index(request):
#     return HttpResponse('Hello, world. You\'re at the blog index.')

def index(request):
    context = {
        'title': 'Блог',
        'data': 'Какой-то текст',
        'name': 'Alex',
        'age': 40,
        'authors': [{'name': 'Alex1', 'age': 41}, {'name': 'Alex2', 'age': 42}, {'name': 'Alex3', 'age': 43}],
    }
    return render(request, "blogapp/index.html", context=context)

def contacts(request):
    return HttpResponse('Moscow.')


def author_create(request):
    for i in range(10):

        author = Author.objects.create(name=f'Author{i}',
                                       age=40 + i,
                                       email=f'Author{i}@mail.ru',
                                       bio=f'bio Author{1}')
        author.save()
    return HttpResponse('Create author')


def authors(request):
    authors = Author.objects.all()
    return render(request, "blogapp/authors.html", context={'authors': authors})