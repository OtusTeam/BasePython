from django.shortcuts import render
from .models import Animal


def index_view(request):
    animals = Animal.objects.all()
    return render(request, 'mainapp/index.html', {'animals': animals})