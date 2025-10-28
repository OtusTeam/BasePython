from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(attrs={"class": "form-control", 'placeholder': 'Введите Email'}),
    )

    class Meta:
        model = get_user_model()
        fields = ('email',)

    def clean_email(self):
        email = self.cleaned_data.get('email').lower()
        User = get_user_model()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Этот email уже занят')
        return email


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(attrs={"class": "form-control", 'placeholder': 'Введите Email'}),
    )

    def clean_username(self):
        username = self.cleaned_data.get('username').lower()
        return username