from django.contrib.auth.forms import UserCreationForm
from .models import MyUser


class RegisterForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = ('username', 'email', 'password1', 'password2')
