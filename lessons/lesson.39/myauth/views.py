from django.views.generic import CreateView

from myauth.forms import MyUserCreateForm
from myauth.models import OtusUser


class MyUserCreateView(CreateView):
    model = OtusUser
    success_url = '/'
    form_class = MyUserCreateForm
    # fields = ('username', 'email', 'password1', 'password2')
