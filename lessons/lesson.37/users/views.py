from django.shortcuts import render
from django.views.generic import CreateView

from users.forms import MyUserCreateForm
from users.models import MyUser


class MyUserCreateView(CreateView):
    model = MyUser
    success_url = '/'
    form_class = MyUserCreateForm
    # template_name =


def logout_confirm(request):
    return render(request, 'registration/logout.html')
