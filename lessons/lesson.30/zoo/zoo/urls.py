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
from django.urls import path
from animals.views import index_view, status_view, contact_view, AnimalsListView, \
    AnimalDetailView, AnimalCreateView, AnimalDeleteView, AnimalUpdateView, ContactFormView
from users.views import UserCreateView, AuthView, MyUserLogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AnimalsListView.as_view()),
    path('animal/<int:pk>/', AnimalDetailView.as_view()),
    path('animal/delete/<int:pk>/', AnimalDeleteView.as_view()),
    path('animal/update/<int:pk>/', AnimalUpdateView.as_view()),
    path('animal/create/', AnimalCreateView.as_view()),
    path('task/', status_view),
    path('contacts/', ContactFormView.as_view()),
    path('register/', UserCreateView.as_view()),
    path('login/', AuthView.as_view()),
    path('logout/', MyUserLogoutView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
