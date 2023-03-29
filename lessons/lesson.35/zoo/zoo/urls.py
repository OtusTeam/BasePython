"""zoo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
# from mainapp.views import index_view, contact_view, get_task_result_view
from mainapp import views
from django.conf import settings
from django.conf.urls.static import static
from userapp.views import RegisterView, LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view),
    path('contact/', views.contact_view),
    path('task-result/<str:task_id>/', views.get_task_result_view),
    path('__debug__/', include('debug_toolbar.urls')),
    # CRUD
    path('category-list/', views.CategoryListView.as_view()),
    path('category-detail/<int:pk>/', views.CategoryDetailView.as_view()),
    path('category-create/', views.CategoryCreateView.as_view()),
    path('category-update/<int:pk>/', views.CategoryUpdateView.as_view()),
    path('category-delete/<int:pk>/', views.CategoryDeleteView.as_view()),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
