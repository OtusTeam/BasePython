from django.contrib import admin
from .models import CustomUser
from django_celery_beat.models import PeriodicTask, IntervalSchedule

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass