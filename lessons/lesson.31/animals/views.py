from django.shortcuts import render
from .models import Category, Animal

def index_view(request):
    animals = Animal.objects.all()
    context = {
        'animals': animals
    }
    return render(request, 'animals/index.html', context)
