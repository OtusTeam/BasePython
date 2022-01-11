# from django.contrib.auth.views import LoginView
from django.views.generic import CreateView

# class ZooUserLoginView(LoginView):
#     pass
from zauth.forms import ZooUserCreateForm
from zauth.models import ZooUser


class ZooUserCreateView(CreateView):
    model = ZooUser
    success_url = '/'
    form_class = ZooUserCreateForm
    # fields = ('username', 'password1', 'password2')
