from django.contrib import admin

from shop_app.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = "title", "description", "price"
