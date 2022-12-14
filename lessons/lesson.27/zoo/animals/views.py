from django.shortcuts import render

from animals.models import Animal


def main_page(request):
    animals = Animal.objects.all()
    context = {
        # 'animals': [
        #     {'kind': 'monkey'},
        #     {'kind': 'bear'},
        #     {'kind': 'rabbit'},
        # ],
        'animals': animals
    }
    return render(request, 'animals/index.html', context=context)
