from django.contrib import admin
from django.contrib.admin import ModelAdmin

from animals.models import Animal, AnimalKind, AnimalFood, AnimalDetail

admin.site.register(Animal)
admin.site.register(AnimalKind)


class FoodModelAdmin(ModelAdmin):
    pass


admin.site.register(AnimalFood, FoodModelAdmin)
admin.site.register(AnimalDetail)
