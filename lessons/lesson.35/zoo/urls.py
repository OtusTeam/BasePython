"""zoo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
import animals.views as animals_views
from zoo import settings

urlpatterns = [
    # path('', animals_views.index),
    path('', animals_views.AnimalsList.as_view()),
    path('animal/create/', animals_views.AnimalCreate.as_view()),
    # path('animal/<int:pk>/', animals_views.animal),
    path('animal/<int:pk>/', animals_views.AnimalDetail.as_view()),

    path('send/', animals_views.send_mail),
    path('result/<str:task_id>/', animals_views.task_status),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns.append(
        path("__debug__/", include("debug_toolbar.urls")),
    )
