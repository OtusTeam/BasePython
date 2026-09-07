from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    """Форма для регистрации нового пользователя."""

    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Enter Email"}
        ),
    )

    class Meta:
        model = get_user_model()
        fields = ("email",)

    def clean_email(self):
        """Проверка email."""
        email = self.cleaned_data.get("email").lower()
        User = get_user_model()  # pylint: disable=C0103
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already registered.")
        return email


class CustomAuthenticationForm(AuthenticationForm):
    """Форма для входа по email."""

    username = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Enter Email"}
        ),
    )

    def clean_username(self):
        username = self.cleaned_data.get("username").lower()
        return username
