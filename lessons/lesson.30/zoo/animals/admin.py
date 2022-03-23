from django.contrib import admin

from .models import Animal, AnimalKind, AnimalDetail, AnimalFood

admin.site.register(Animal)
admin.site.register(AnimalKind)
admin.site.register(AnimalDetail)
admin.site.register(AnimalFood)
