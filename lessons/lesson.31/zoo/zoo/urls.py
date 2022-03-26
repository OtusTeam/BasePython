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

import animals.views as animal
from zoo.settings import DEBUG

urlpatterns = [
    path('', animal.index, name='main'),
    # path('status/', animal.task_status),
    path('status/<str:task_id>/', animal.task_status, name='task_status'),
    # path('status/<str:task_id>/<int:page_num>/', animal.task_status),

    # path('animal/detail/<int:pk>/', animal.animal_detail, name='animal_detail'),
    path('animal/detail/<int:pk>/', animal.AnimalDetailView.as_view(), name='animal_detail'),
    path('animal/create/', animal.AnimalCreateView.as_view(), name='animal_create'),
    path('animal/update/<int:pk>/', animal.AnimalUpdateView.as_view(), name='animal_update'),

    path('admin/', admin.site.urls),
]

if DEBUG:
    urlpatterns += path('__debug__/', include('debug_toolbar.urls')),
