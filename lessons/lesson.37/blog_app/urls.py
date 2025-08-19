from django.urls import path
from blog_app.views import index, about


urlpatterns = [
    path('', index),
    path('about/', about)
]
