from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Animal, AnimalKind


def animals_list(request: HttpRequest) -> HttpResponse:
    animals = (
        Animal
        .objects
        .order_by("pk")
        # .prefetch_related("kind")
        .select_related("kind")
        .all()
    )
    return render(
        request=request,
        template_name="animals/index.html",
        context={"animals": animals},
    )


def animal_kinds_with_animals(request: HttpRequest) -> HttpResponse:
    animal_kinds = (
        AnimalKind
        .objects
        # .prefetch_related("animal_set")
        .prefetch_related("animals")
        # .select_related("animals")
        .order_by("pk")
        .all()
    )
    return render(
        request=request,
        template_name="animals/animal_kids.html",
        context={"animal_kinds": animal_kinds},
    )

