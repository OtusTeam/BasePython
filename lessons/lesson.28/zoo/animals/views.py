from django.http import HttpRequest
from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Animal


def index(request: HttpRequest):
    animals = Animal.objects.select_related("kind").order_by("id").all()
    # return HttpResponse(f"<h1>Hello page {request.path}</h1>")
    context = {
        "animals": animals,
    }
    return render(request, "animals/index.html", context=context)


def details(request: HttpRequest, pk: int):
    animal = get_object_or_404(
        Animal.objects.select_related("kind", "details").prefetch_related("food"),
        pk=pk,
    )
    # animal = get_object_or_404(Animal.objects.select_related(), pk=pk)
    context = {
        "animal": animal,
    }
    return render(request, "animals/details.html", context=context)
