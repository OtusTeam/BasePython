from typing import TYPE_CHECKING

from django.contrib import admin

from .models import Animal, AnimalProfile, AnimalKind, AnimalFood

if TYPE_CHECKING:
    admin.site: admin.AdminSite


@admin.register(AnimalKind, AnimalFood)
class UniversalAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "description"
    list_display_links = "pk", "name",


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):

    def description_short(self, obj: Animal) -> str:
        # obj.description: str
        if len(obj.description) < 40:
            return obj.description
        return obj.description[:38] + "..."

    # list_display = "pk", "name", "kind", "age", "description"
    # list_display = "pk", "name", "kind", "age", "desc_short"
    list_display = "pk", "name", "kind", "age", "description_short", "archived"
    list_display_links = "pk", "name",
    ordering = "-pk",
    # ordering = "-name", "pk"


# admin.site.register(Animal, AnimalAdmin)


@admin.register(AnimalProfile)
class AnimalProfileAdmin(admin.ModelAdmin):
    list_display = "pk", "origin", "biography"
    list_display_links = "pk", "origin",


# @admin.register(AnimalFood)
# class AnimalFoodAdmin(admin.ModelAdmin):
#     list_display = "pk", "name", "description"
#     list_display_links = "pk", "name",
