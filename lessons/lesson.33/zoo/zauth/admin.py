from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from zauth.models import ZooUser


# admin.site.register(ZooUser)
class ZooUserAdmin(UserAdmin):
    pass


admin.site.register(ZooUser, ZooUserAdmin)
