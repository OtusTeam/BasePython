from django.shortcuts import render
from .models import Animal


def index_view(request):
    # animals = Animal.objects.all().select_related('category')
    animals = Animal.objects.all().select_related('category').prefetch_related('category__foods')
    # animals = Animal.objects.all().prefetch_related('category__foods')

    return render(request, 'mainapp/index.html', {'animals': animals})