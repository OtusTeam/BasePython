from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404

from .models import Animal


def index(request: HttpRequest):
    context = {
        "animals": (
            Animal
                .objects
                .select_related("kind")
                .prefetch_related("food")
                .order_by("pk")
                .all()
        ),
    }
    return render(request=request, template_name="animals/index.html", context=context)


def details(request: HttpRequest, pk: int):
    animal = get_object_or_404(
        (
            Animal
            .objects
            # .select_related()
            # .select_related("profile")
            # .select_related("kind")
            .select_related("profile", "kind")
            .prefetch_related("food")
        ),
        pk=pk,
    )
    # print(animal.food)
    # print(animal.food.all)
    # food = animal.food.all()
    # print(food)
    context = {
        "animal": animal,
    }
    return render(request=request, template_name="animals/details.html", context=context)
