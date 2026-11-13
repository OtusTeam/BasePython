from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    """Форма для регистрации нового пользователей на основе кастомной модели."""
    email = forms.EmailField(
        required=True,
        label='Электронная почта',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите вашу электронную почту'})
    )

    class Meta:
        model = get_user_model()
        fields = ('email',)

    def clean_email(self):
        """Проверяет, существует ли пользователь с таким email."""
        email = self.cleaned_data.get('email').lower()
        User = get_user_model()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким email уже существует')
        return email


class CustomAuthenticationForm(AuthenticationForm):
    """Форма для аутентификации пользователей на основе кастомной модели."""
    username = forms.EmailField(
        required=True,
        label='Электронная почта',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите вашу электронную почту'})
    )

    def clean_username(self):
        """Можно добаить дополнительную проверку."""
        username = self.cleaned_data.get('username').lower()
        return username