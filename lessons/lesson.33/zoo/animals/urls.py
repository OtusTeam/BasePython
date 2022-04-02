from django.urls import path

import animals.views as animal

app_name = 'animals'

urlpatterns = [
    path('detail/<int:pk>/', animal.AnimalDetailView.as_view(), name='detail'),
    path('create/', animal.AnimalCreateView.as_view(), name='create'),
    path('update/<int:pk>/', animal.AnimalUpdateView.as_view(), name='update'),
]
