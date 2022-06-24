from django.contrib import admin

from .models import Animal, AnimalKind, AnimalDetail, AnimalFood


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'kind')
    list_display_links = ('id', 'name')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related("kind")


@admin.register(AnimalDetail)
class AnimalDetailAdmin(admin.ModelAdmin):
    list_display = ("bio_short", "animal")
    list_display_links = ("bio_short",)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related("animal")

    def bio_short(self, obj: AnimalDetail):
        if len(obj.biography) < 50:
            return obj.biography
        return obj.biography[:50] + "..."


admin.site.register(Animal, AnimalAdmin)
admin.site.register(AnimalKind)
# admin.site.register(AnimalDetail, AnimalDetailAdmin)
admin.site.register(AnimalFood)
