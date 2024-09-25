from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)

from .models import Task


class TasksListView(ListView):
    model = Task


class TaskDetailView(DetailView):
    model = Task


class TaskCreateView(CreateView):
    model = Task
    fields = (
        "title",
        "description",
    )
    # template_name = "custom-template-name.html"
    # context_object_name = "task"
    # context_object_name = "assignment"
