from django.urls import path

from .views import (
    index,
    details,
    get_task,
    AnimalsListView,
    AnimalDetailView,
    AnimalKindListView,
    AnimalsByKindListView,
    AnimalKindDeleteView,
    AnimalKindCreateView,
    AnimalDeleteView,
    AnimalCreateView,
)

app_name = "animals"

urlpatterns = [
    # path("", index, name="index"),
    path("", AnimalsListView.as_view(), name="index"),
    path("create/", AnimalCreateView.as_view(), name="create"),
    # path("<int:pk>/", details, name="details"),
    path("kinds/", AnimalKindListView.as_view(), name="kinds"),
    path("kinds/create/", AnimalKindCreateView.as_view(), name="create-kind"),
    # path("kinds/<int:pk>/", AnimalKindListView.as_view(), name="kinds"),
    path("kinds/<int:pk>/confirm-delete/", AnimalKindDeleteView.as_view(), name="delete-kind"),

    path("<int:pk>/", AnimalDetailView.as_view(), name="details"),
    path("<int:pk>/confirm-delete/", AnimalDeleteView.as_view(), name="delete"),
    # path("get-task/<str:task_id>/", get_task, name="task-status"),
    path("<animal_kind>/", AnimalsByKindListView.as_view(), name="by-kind"),
]
