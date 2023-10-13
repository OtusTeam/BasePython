from django.urls import path

import main.views as main

app_name = 'main'

urlpatterns = [
    path('', main.AnimalsList.as_view(), name='index'),
    path('create/', main.AnimalsCreate.as_view(), name='create'),
]
# index
# animals:index
# staff:index
