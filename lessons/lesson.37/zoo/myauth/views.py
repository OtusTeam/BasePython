from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView

from myauth.forms import MyUserCreateForm
from myauth.models import MyUser


class MyUserCreateView(CreateView):
    model = User
    success_url = '/'
    form_class = MyUserCreateForm
    # model = MyUser
    # form_class = MyUserCreateForm

