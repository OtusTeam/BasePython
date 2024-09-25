from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.TasksListView.as_view(), name="list"),
    path("<int:pk>/", views.TaskDetailView.as_view(), name="detail"),
    path("create/", views.TaskCreateView.as_view(), name="create"),
]
