from django.urls import path

from .views import animals_list, animal_kinds_with_animals

urlpatterns = [
    path("", animals_list),
    path("kinds/", animal_kinds_with_animals),
]
