from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = "user", "birth_date", "address"
    list_display_links = "user", "birth_date", "address"
