from django.contrib import admin

from .models import Animal, AnimalKind


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "age", "kind"
    list_display_links = "pk", "name"


@admin.register(AnimalKind)
class AnimalKindAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "description"
    list_display_links = "pk", "name"
