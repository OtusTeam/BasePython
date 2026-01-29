from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog_app.urls')),
    path('user/', include('user_app.urls')),
]
