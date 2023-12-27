from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from celery.result import AsyncResult

from .models import Animal, Category
from .tasks import send_contact_email


def index_view(request):
    animals = Animal.objects.select_related("category").prefetch_related("meals").all()
    context = {
        "animals": animals,
    }
    return render(
        request,
        "animals/animals-list.html",
        context,
    )


def categories_with_animals(request: HttpRequest):
    context = {"categories": (Category.objects.prefetch_related("animals").all())}
    return render(
        request,
        "animals/categories-with-animals.html",
        context,
    )


def contact_view(request: HttpRequest):
    if request.method == "POST":
        message = request.POST["message"]
        # send_contact_email(message)
        result = send_contact_email.delay(message)
        print("RESULT", result)
        print(type(result))
        print(result.state)
        print(result.ready())

        task_id = result.id
        url = f'{reverse("animals:status")}?id={task_id}'
        return HttpResponseRedirect(url)

    return render(request, "animals/contact.html")


def status_view(request):
    id = request.GET.get("id")
    # get current status
    res = AsyncResult(id)
    is_ready = res.ready()
    status = res.state
    result = res.result
    context = {"id": id, "is_ready": is_ready, "status": status, "result": result}
    return render(request, "animals/status.html", context)
