from django.urls import path
from django.views.generic import TemplateView

import animals.views as animals

app_name = 'animals'

urlpatterns = [
    path('', animals.index, name='index'),
    # path('animals/', animals.animals_list, name='animals_list'),
    path('animals/',
         animals.AnimalsListView.as_view(),
         name='animals_list'),
    path('animals/create/',
         animals.AnimalKindCreateView.as_view(),
         name='animalkind_create'),
    path('animals/update/<int:item_pk>/',
         animals.AnimalKindUpdateView.as_view(),
         name='animalkind_update'),

    # path('about/', animals.about, name='about'),
    path('about/',
         TemplateView.as_view(template_name='animals/about.html'),
         name='about'),

    path('status/<str:task_id>/', animals.status_view, name='status_view'),
]
