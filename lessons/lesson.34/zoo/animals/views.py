from datetime import datetime

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, CreateView

from zoo import celery_app
from celery.result import AsyncResult
from django.http import HttpRequest, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import AnimalCreateForm
from .models import Animal, AnimalKind
from .tasks import notify_animal_created


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

    if settings.CELERY_TASKS_ENABLED:
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


#


class AnimalsListView(ListView):
    # template_name = "animals/index.html"
    template_name = "animals/animal_list.html"
    context_object_name = "animals"
    queryset = (
        Animal
            .objects
            .select_related("kind")
            .prefetch_related("food")
            .filter(archived=False)
            .order_by("pk")
            .all()
    )


class AnimalDetailView(DetailView):
    template_name = "animals/details.html"
    context_object_name = "animal"
    queryset = (
        Animal
        .objects
        .select_related("profile", "kind")
        .prefetch_related("food")
    )


class AnimalKindListView(ListView):
    model = AnimalKind


class AnimalsByKindListView(ListView):
    queryset = Animal.objects.select_related("kind")

    def get_queryset(self):
        qs = super().get_queryset()
        kind_name = self.kwargs["animal_kind"]
        kind: AnimalKind = get_object_or_404(AnimalKind, name=kind_name)
        # return qs.filter(kind__name=kind_name)
        # return qs.filter(kind__name=kind.name)
        return qs.filter(kind=kind)


class AnimalKindCreateView(CreateView):
    model = AnimalKind
    fields = ["name", "description"]
    success_url = reverse_lazy("animals:kinds")


class AnimalKindDeleteView(DeleteView):
    model = AnimalKind
    success_url = reverse_lazy("animals:kinds")
    context_object_name = "kind"


class AnimalCreateView(LoginRequiredMixin, CreateView):
    model = Animal
    form_class = AnimalCreateForm

    def get_success_url(self):
        return reverse("animals:details", kwargs={"pk": self.object.pk})


class AnimalDeleteView(PermissionRequiredMixin, DeleteView):
    model = Animal
    success_url = reverse_lazy("animals:index")
    context_object_name = "animal"

    permission_required = "animals.delete_animal"
    # permission_denied_message = ""

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)
