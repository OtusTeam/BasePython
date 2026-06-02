from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    """Форма для регистрации нового пользователя."""
    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'})
    )

    class Meta:
        model = get_user_model()
        fields = ('email', )

    def clean_email(self):
        email = self.cleaned_data.get('email').lower()
        UserModel = get_user_model()
        if UserModel.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already registered.')
        return email


class CustomAuthenticationForm(AuthenticationForm):
    """Форма для входа"""
    username = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'})
    )

    def clean_username(self):
        username = self.cleaned_data.get('username').lower()
        return username
