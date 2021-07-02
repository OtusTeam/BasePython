from django.contrib import admin
from django.urls import path, include
from animals.views import index_view, status_view, contact_view, AnimalsListView, \
    AnimalDetailView, AnimalCreateView, AnimalDeleteView, AnimalUpdateView, ContactFormView, FoodListView
from users.views import UserCreateView, AuthView, MyUserLogoutView
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AnimalsListView.as_view(), name='index'),
    path('food/', FoodListView.as_view(), name='food'),
    path('animal/<int:pk>/', AnimalDetailView.as_view()),
    path('animal/delete/<int:pk>/', AnimalDeleteView.as_view()),
    path('animal/update/<int:pk>/', AnimalUpdateView.as_view()),
    path('animal/create/', AnimalCreateView.as_view()),
    path('task/', status_view),
    path('contacts/', ContactFormView.as_view()),
    # users
    path('users/', include('users.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
