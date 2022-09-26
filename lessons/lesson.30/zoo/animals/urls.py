from django.urls import path

from .views import index, details, get_task

app_name = "animals"

urlpatterns = [
    path("", index, name="index"),
    path("<int:pk>/", details, name="details"),
    path("get-task/<str:task_id>/", get_task, name="task-status"),
]
