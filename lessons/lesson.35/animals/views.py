from django.shortcuts import render
from .models import Animal


def animals_list_view(request):
    animals = Animal.objects.select_related('category').prefetch_related('food').all()
    return render(request, 'animals/list.html', {'animals': animals})
