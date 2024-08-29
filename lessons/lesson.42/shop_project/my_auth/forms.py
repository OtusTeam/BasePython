from django.contrib.auth.forms import UserCreationForm

from .models import ShopUser


class ShopUserCreateForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'email', 'password1', 'password2')
