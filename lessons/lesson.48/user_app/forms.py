from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):  # pylint:disable=too-many-ancestors
    """Форма для регистрации нового пользователя."""

    email = forms.EmailField(
        required=True,
        label="Электронная почта",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Введите email"}
        ),
    )

    class Meta:
        model = get_user_model()
        fields = ("email",)

        def clean_email(self):
            email = self.cleaned_data["email"].lower()
            User = get_user_model()
            if User.objects.filter(emailt=email).exists():
                raise forms.ValidationError("Этот email уже занят")
            return email


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        required=True,
        label="Электронная почта",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Введите email"}
        ),
    )

    def clean_username(self):
        username = self.cleaned_data["username"].lower()
        return username
