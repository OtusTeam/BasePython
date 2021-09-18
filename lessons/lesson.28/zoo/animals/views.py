from django.shortcuts import render

# FBV -> CBV
from animals.models import Animal


def index_view(request):
    animals = Animal.objects.all()
    return render(request,
                  'animals/index.html',
                  {'animals': animals})
