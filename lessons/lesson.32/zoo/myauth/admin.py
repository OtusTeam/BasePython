from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserAdminGeneric

from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = "pk", "user", "bio"

# from .models import MyCustomUser
#
#
# @admin.register(MyCustomUser)
# class UserAdmin(UserAdminGeneric):
#     # list_display = (*UserAdminGeneric.list_display, "bio")
#     fieldsets = (
#         *UserAdminGeneric.fieldsets,
#         ("Extra", {
#             "fields": ("bio", ),
#         })
#     )
