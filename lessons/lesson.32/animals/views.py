from django.http import HttpRequest
from django.shortcuts import render
from .models import Animal, Category


def index_view(request):
    animals = (
        Animal
        .objects
        .select_related("category")
        .prefetch_related("meals")
        .all()
    )
    context = {
        "animals": animals,
    }
    return render(
        request,
        "animals/animals-list.html",
        context,
    )


def categories_with_animals(request: HttpRequest):
    context = {
        "categories": (
            Category
            .objects
            .prefetch_related("animals")
            .all()
        )
    }
    return render(
        request,
        "animals/categories-with-animals.html",
        context,
    )
