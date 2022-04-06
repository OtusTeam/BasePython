from django.contrib.auth.forms import UserCreationForm

from myauth.models import MyUser


class MyUserCreateForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('username', 'email', 'password1', 'password2')
