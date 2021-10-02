from django.contrib import admin

from animals.models import Animal, AnimalKind

admin.site.register(Animal)
admin.site.register(AnimalKind)
