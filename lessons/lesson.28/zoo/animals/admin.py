from typing import TYPE_CHECKING

from django.contrib import admin

from .models import Animal

if TYPE_CHECKING:
    admin.site: admin.AdminSite


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):

    def description_short(self, obj: Animal) -> str:
        # obj.description: str
        if len(obj.description) < 40:
            return obj.description
        return obj.description[:38] + "..."

    # list_display = "pk", "name", "kind", "age", "description"
    # list_display = "pk", "name", "kind", "age", "desc_short"
    list_display = "pk", "name", "kind", "age", "description_short"
    list_display_links = "pk", "name",
    ordering = "-pk",
    # ordering = "-name", "pk"


# admin.site.register(Animal, AnimalAdmin)

