from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from users.models import MyUser


# Register your models here.
class MyUserAdmin(UserAdmin):
    pass


admin.site.register(MyUser, UserAdmin)
