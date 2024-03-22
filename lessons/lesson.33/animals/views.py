from django.shortcuts import render
# from django.db import connection

from animals.models import Animal


def index(request):
    # animals_qty = len(
    #     Animal.objects.all(),  # db level -> python 1000 -> inst Animal
    # )
    animals_qty = Animal.objects.count()  # db level -> COUNT()
    animals = Animal.objects.all()
    # animals = Animal.objects.filter(
    #     name__startswith='po',
    #     # age__gte=3,
    # )
    # print(dir(animals))
    # print(animals.query)
    # animals = [
    #     {'name': 'King', 'kind': 'lion'}
    # ]

    context = {
        'animals': animals,
        'animals_qty': animals_qty,
    }

    return render(request, 'animals/index.html', context=context)
