from django.urls import path

from .views import index, details, task_status

app_name = "animals"

urlpatterns = [
    path("", index, name="list"),
    path("<int:pk>/", details, name="details"),
    path("<str:task_id>/", task_status, name="task-status"),
]
