from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

from blogapp.models import Author


# Create your views here.

# Семинар 1
# def index(request):
#     return HttpResponse('Hello, world. You\'re at the blog index.')

def index(request):
    
    text = """Internationalization and localization¶
Django offers a robust internationalization and localization framework to assist you in the development of applications for multiple languages and world regions:

Overview | Internationalization | Localization | Localized web UI formatting and form input
Time zones
Performance and optimization¶
There are a variety of techniques and tools that can help get your code running more efficiently - faster, and using fewer system resources.

Performance and optimization overview
Geographic framework¶
GeoDjango intends to be a world-class geographic web framework. Its goal is to make it as easy as possible to build GIS web applications and harness the power of spatially enabled data."""
    
    context = {
        'title': 'Блог',
        'data':  text,
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


def author(request, author_id):
    # try:
    #     author = Author.objects.get(id=author_id)
    # except Author.DoesNotExist:
    #     return HttpResponseNotFound('<h2>Author not found</h2>')
    # # print(author)
    author = get_object_or_404(Author, id=author_id)
    return render(request, "blogapp/author.html", context={'author': author})

