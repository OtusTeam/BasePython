from django.contrib.auth.forms import (
    AuthenticationForm as AuthenticationFormGeneric,
    UserCreationForm as UserCreationFormGeneric,
)
from django.forms import Widget

from .models import UserModel


class FormStylesMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            # print(name, field, field.widget)
            widget: Widget = field.widget
            widget.attrs["class"] = "form-control"


class UserCreationForm(FormStylesMixin, UserCreationFormGeneric):

    class Meta:
        model = UserModel
        fields = "username", "email", "password1", "password2"


class AuthenticationForm(FormStylesMixin, AuthenticationFormGeneric):
    pass
