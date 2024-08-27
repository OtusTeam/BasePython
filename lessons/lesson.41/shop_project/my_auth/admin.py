from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import ShopUser


class ShopUserAdmin(UserAdmin):
    pass


admin.site.register(ShopUser, ShopUserAdmin)
