from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = "id", "title", "description", "done"
    list_display_links = "id", "title",
