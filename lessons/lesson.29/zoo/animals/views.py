from django.http import HttpRequest
from django.shortcuts import render, HttpResponse, get_object_or_404

from celery.result import AsyncResult
from .models import Animal
from .tasks import new_animal_created_notification


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


def task_status(request: HttpRequest, task_id: str):
    task: AsyncResult = new_animal_created_notification.AsyncResult(task_id)

    print(task, task.id, task.status, task.backend, task._get_task_meta())
    context = {
        "task_id": task_id,
        "status": task.status,
        "backend": task.backend,
    }
    return render(request, "animals/task_status.html", context=context)

