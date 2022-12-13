from django.shortcuts import render

from animals.models import Food


def main_page(request):
    foods = Food.objects.all()
    context = {
        # 'animals': [
        #     {'kind': 'monkey'},
        #     {'kind': 'bear'},
        #     {'kind': 'rabbit'},
        # ],
        'foods': foods
    }
    return render(request, 'animals/index.html', context=context)
