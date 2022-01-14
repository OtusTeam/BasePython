from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

import zauth.views as zauth

app_name = 'zauth'

urlpatterns = [
    path('user/create/',
         zauth.ZooUserCreateView.as_view(),
         name='user_create'),
    path('login/',
         LoginView.as_view(),
         name='login'),
    path('logout/',
         LogoutView.as_view(),
         name='logout'),
    # path('logout/', zauth, name='logout'),

]
