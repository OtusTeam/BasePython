from django.http import HttpRequest
from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Animal


def index(request: HttpRequest):
    # print(request.path)
    # print(request.method)
    # print(request.GET)
    # # print(request.META)
    # return HttpResponse(f"<h1>Hello path <code>{request.path}</code></h1>")

    context = {
        "animals": Animal.objects.order_by("pk").all()
    }
    return render(request=request, template_name="animals/index.html", context=context)


def details(request: HttpRequest, pk: int):
    context = {
        "animal": get_object_or_404(Animal, pk=pk),
    }
    return render(request=request, template_name="animals/details.html", context=context)
