from django.contrib import admin
from django.urls import path, include

import animals.views as animal
from zoo.settings import DEBUG

urlpatterns = [
    path('', animal.index, name='main'),
    path('status/<str:task_id>/', animal.task_status, name='task_status'),

    path('animal/', include('animals.urls', namespace='animals')),
    path('myauth/', include('myauth.urls', namespace='myauth')),

    path('admin/', admin.site.urls),
]

if DEBUG:
    urlpatterns += path('__debug__/', include('debug_toolbar.urls')),
