from datetime import datetime

from zoo import celery_app
from celery.result import AsyncResult
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, get_object_or_404

from .models import Animal
from .tasks import log_animals_details_access, notify_animal_created


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
    # log_animals_details_access(path=request.path, pk=pk)
    # log_animals_details_access.delay(path=request.path, pk=pk)

    animal = get_object_or_404(
        (
            Animal
            .objects
            .select_related("profile", "kind")
            .prefetch_related("food")
        ),
        pk=pk,
    )

    task: AsyncResult = notify_animal_created.delay(
        animal_name=animal.name,
        path=request.path,
        created_at=str(datetime.now()),
    )
    print("created task", task and task.id, task._get_task_meta())

    context = {
        "animal": animal,
    }
    return render(request=request, template_name="animals/details.html", context=context)


def get_task(request: HttpRequest, task_id: str):
    task_result: AsyncResult = notify_animal_created.AsyncResult(task_id)
    # task_result = AsyncResult(
    #     task_id,
    #     app=celery_app,
    # )
    # print(task_result.get())
    # task_result: AsyncResult = celery_app.AsyncResult(task_id)
    print(task_result, task_result.backend, task_result.name, task_result._get_task_meta())
    return JsonResponse({
        "task_id": task_id,
        "status": task_result.status,
    })
