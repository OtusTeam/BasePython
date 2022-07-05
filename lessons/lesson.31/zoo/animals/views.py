from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView, DeleteView, CreateView

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from celery.result import AsyncResult
from zoo import celery_app

from .models import Animal, AnimalKind
from .forms import AnimalCreateForm


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
    task: AsyncResult = celery_app.AsyncResult(task_id)

    print(task, task.id, task.status, task.backend, task._get_task_meta())
    context = {
        "task_id": task_id,
        "status": task.status,
        "backend": task.backend,
    }
    return render(request, "animals/task_status.html", context=context)


class AnimalsListView(ListView):
    # model = Animal
    queryset = Animal.objects.select_related("kind")
    # template_name = "animals/animal_list.html"
    context_object_name = "animals"


class AnimalKindListView(ListView):
    # model = Animal
    queryset = Animal.objects.select_related("kind")

    def get_queryset(self):
        qs = super().get_queryset()
        # return qs.filter(kind__name=self.kwargs["kind_name"])
        kind: AnimalKind = get_object_or_404(AnimalKind, name=self.kwargs["kind_name"])
        # return qs.filter(kind__id=kind.id)
        return qs.filter(kind__name=kind.name)


class AnimalDetailView(DetailView):
    # model = Animal
    queryset = Animal.objects.select_related("kind", "details").prefetch_related("food")

    # template_name = "animals/animal_detail.html"
    template_name = "animals/details.html"


class AnimalDeleteView(PermissionRequiredMixin, DeleteView):
    model = Animal
    success_url = reverse_lazy("animals:list")
    # template_name_suffix = "_confirm_delete"

    # permission_required = ("animals.delete_animal", )
    permission_required = "animals.delete_animal"

    # def has_permission(self):
    #     perms = self.request.user.get_all_permissions()
    #     print("user perms", perms)
    #     return super().has_permission()


class AnimalCreateView(LoginRequiredMixin, CreateView):
    model = Animal
    # fields = ["name", "age", "kind", "description"]
    form_class = AnimalCreateForm

    def get_success_url(self):
        return reverse("animals:details", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        self.object: Animal = form.save(commit=False)
        self.object.created_at = timezone.now()
        self.object.save()
        return super().form_valid(form)


class AnimalKindsListView(ListView):
    # model = AnimalKind
    queryset = AnimalKind.objects.filter(deleted=False)
    template_name = "animals/animal_kinds.html"
    # context_object_name = "kind"


class AnimalKindDeleteView(DeleteView):
    model = AnimalKind
    template_name = "animals/animal_kind_confirm_delete.html"
    context_object_name = "kind"
    success_url = reverse_lazy("animals:animal-kinds")

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object: AnimalKind
        self.object.deleted = True
        self.object.save()
        return HttpResponseRedirect(success_url)
