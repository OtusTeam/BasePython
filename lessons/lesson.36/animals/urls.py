"""
URL configuration for settings project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views

app_name = "animals"

urlpatterns = [
    path(
        "",
        views.index_view,
        name="index",
    ),
    path(
        "categories/",
        views.categories_with_animals,
        name="categories-with-animals",
    ),
    path(
        "contact/",
        views.contact_view,
        name="contact",
    ),
    path(
        "status/",
        views.status_view,
        name="status",
    ),
    path(
        "list/",
        views.AnimalListView.as_view(),
        name="list",
    ),
    path(
        "detail/<int:pk>/",
        views.AnimalDetailView.as_view(),
        name="detail",
    ),
    path(
        "create/",
        views.AnimalCreateView.as_view(),
        name="create",
    ),
    path(
        "update/<int:pk>/",
        views.AnimalUpdateView.as_view(),
        name="update",
    ),
    path(
        "delete/<int:pk>/",
        views.AnimalDeleteView.as_view(),
        name="delete",
    ),
    path(
        "about/",
        views.AboutTemplateView.as_view(),
        name="about",
    ),
]
