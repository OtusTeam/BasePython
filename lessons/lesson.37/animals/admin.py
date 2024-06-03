from django.contrib import admin
from .models import Category, Animal, Card, Food

# Register your models here.
admin.site.register(Category)
admin.site.register(Animal)
admin.site.register(Card)
admin.site.register(Food)
