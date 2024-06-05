from django.contrib import admin
from django.urls import path, include
from contacts.views import contact_view, status_view

urlpatterns = [
    path('', include('animals.urls')),
    path('admin/', admin.site.urls),
    path('contacts/', contact_view),
    path('status/<str:task_id>/', status_view),
    path("__debug__/", include("debug_toolbar.urls")),
]
