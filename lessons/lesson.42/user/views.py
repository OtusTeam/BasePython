from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.
def create_user_view(request):
    user = User.objects.create_user(username='test_user',
                                    password='test_password',
                                    email='test@mail.ru'

                                    )
    return HttpResponse(f'Пользователь создан: {user.username}')


class RegistrationView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'user/registration.html'
