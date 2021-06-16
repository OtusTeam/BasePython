from django.http import Http404
from django.shortcuts import render
from .models import Animal


# Create your views here.
def index_view(request):
    if request.method == 'GET':
        animals = Animal.objects.all()
        return render(request, 'animals/index.html', {'animals': animals})
    else:
        raise Http404

    # Flask
    # return render(request, 'animals/index.html', animals=animals)
    # return render(request, 'animals/index.html', **{'animals': animals})
