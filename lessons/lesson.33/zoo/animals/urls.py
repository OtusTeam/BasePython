from django.urls import path

from .views import (
    index,
    details,
    task_status,
    AnimalsListView,
    AnimalKindListView,
    AnimalDetailView,
    AnimalDeleteView,
    AnimalCreateView,
    AnimalKindsListView,
    AnimalKindDeleteView,
)

app_name = "animals"

urlpatterns = [
    path("kinds/", AnimalKindsListView.as_view(), name="animal-kinds"),
    path("kinds/<int:pk>/confirm-delete/", AnimalKindDeleteView.as_view(), name="animal-kind-delete"),

    # path("", index, name="list"),
    path("", AnimalsListView.as_view(), name="list"),
    path("create/", AnimalCreateView.as_view(), name="create"),
    path("<int:pk>/", AnimalDetailView.as_view(), name="details"),
    path("<int:pk>/confirm-delete/", AnimalDeleteView.as_view(), name="delete"),

    path("<str:kind_name>/", AnimalKindListView.as_view(), name="kind-list"),
    # path("<int:pk>/", details, name="details"),
    # path("<str:task_id>/status/", task_status, name="task-status"),
]
