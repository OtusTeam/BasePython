from django.contrib import admin
from .models import Animal, Category, Food


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = "id", "name", "category"
    list_display_links = "id", "name"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "id", "name"
    list_display_links = "id", "name"


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = "id", "title"
    list_display_links = "id", "title"
