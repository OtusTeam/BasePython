from django.contrib import admin

from .models import Category
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = "id", "name", "price", "updated_at"
    list_display_links = "id", "name"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "id", "name", "description"
    list_display_links = "id", "name"
