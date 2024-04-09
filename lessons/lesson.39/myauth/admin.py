from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from myauth.models import OtusUser


class OtusUserAdmin(UserAdmin):
    pass


admin.site.register(OtusUser, OtusUserAdmin)
