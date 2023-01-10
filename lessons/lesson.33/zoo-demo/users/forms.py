from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class RegistrationForm(UserCreationForm):

    username = forms.CharField(help_text='')
    password1 = forms.CharField(help_text='', label='password', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')