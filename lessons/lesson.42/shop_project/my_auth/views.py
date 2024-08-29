from django.views.generic import CreateView

from .forms import ShopUserCreateForm
from .models import ShopUser


class ShopUserCreateView(CreateView):
    model = ShopUser
    success_url = '/'
    form_class = ShopUserCreateForm
