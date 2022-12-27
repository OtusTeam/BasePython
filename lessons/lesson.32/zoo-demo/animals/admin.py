from django.contrib import admin

from animals.models import Animal, Card, Category

admin.site.register(Category)
admin.site.register(Animal)
admin.site.register(Card)
