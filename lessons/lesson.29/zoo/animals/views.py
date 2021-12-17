from django.shortcuts import render

from animals.models import Animal


def index(request):
    return render(request, 'animals/index.html')


def animals_list(request):
    # animals = Animal.objects.all()
    animals = Animal.objects.select_related('kind'). \
        prefetch_related('animalfood_set').all()
    context = {
        'animals': animals
    }
    return render(request, 'animals/animals_list.html', context=context)
