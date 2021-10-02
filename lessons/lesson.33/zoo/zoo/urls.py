"""zoo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.views.generic import TemplateView

import animals.views as animals
import myauth.views as myauth
from zoo.settings import DEBUG

urlpatterns = [
    path('', animals.AnimalList.as_view(), name='main_page'),

    path('food/', animals.food_view, name='food_view'),
    path('status/', animals.check_task_status),

    path('animals/', animals.AnimalList.as_view()),
    path('animals/create/', animals.AnimalCreate.as_view(), name='animal_create'),
    path('animals/update/<int:pk>/', animals.AnimalUpdate.as_view(), name='animal_update'),
    path('animals/<int:pk>/', animals.AnimalDetail.as_view(), name='animal_detail'),
    path('animals/delete/<int:pk>/', animals.AnimalDelete.as_view(), name='animal_delete'),

    path('about/', TemplateView.as_view(template_name='animals/contacts.html')),

    # login
    path('auth/login/', myauth.MyLoginView.as_view(), name='login'),
    path('auth/logout/', myauth.MyLogoutView.as_view(), name='logout'),
    path('auth/user/create/',
         myauth.UserCreateView.as_view(),
         name='user_create'),

    path('admin/', admin.site.urls),
]

if DEBUG:
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls)), ]
