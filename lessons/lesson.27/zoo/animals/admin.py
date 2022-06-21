from django.contrib import admin

from .models import Animal


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'kind')
    list_display_links = ('id', 'name')


admin.site.register(Animal, AnimalAdmin)
