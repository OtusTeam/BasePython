from django.contrib import admin
from .models import Category, Animal, Food, Card

# Register your models here.
admin.site.register(Animal)
admin.site.register(Category)
admin.site.register(Food)
admin.site.register(Card)