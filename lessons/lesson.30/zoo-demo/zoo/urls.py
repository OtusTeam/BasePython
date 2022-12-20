"""zoo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from animals import views

urlpatterns = [
    path('', views.main_page),
    path('admin/', admin.site.urls),
    path('animals/', views.AnimalListView.as_view(), name='animals'),
    path('animals/<int:pk>/', views.AnimalDetailView.as_view(), name='animal'),
    path('animals/create/', views.AnimalCreateView.as_view(), name='animal_create'),
    path('animals/update/<int:pk>/', views.AnimalUpdateView.as_view(), name='animal_update'),
    path('animals/delete/<int:pk>/', views.AnimalDeleteView.as_view(), name='animal_delete'),
    path('animals/task-result/<str:task_id>/', views.TaskResultTemplateView.as_view(), name='task_result'),
    path('__debug__/', include('debug_toolbar.urls')),
]
