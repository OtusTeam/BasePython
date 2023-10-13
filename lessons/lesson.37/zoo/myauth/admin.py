from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from myauth.models import MyUser


class MyUserAdmin(UserAdmin):
    pass


# admin.site.register(MyUser, MyUserAdmin)
admin.site.register(MyUser, UserAdmin)
