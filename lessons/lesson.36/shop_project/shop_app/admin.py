import textwrap

from django.contrib import admin

# from shop_app.models import Category
from .models import Category, Product, Order, OrderProduct


class ShortDescriptionMixin:

    @classmethod
    def short_description(cls, obj: Category) -> str:
        return textwrap.shorten(obj.description, width=50)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin, ShortDescriptionMixin):
    list_display = "pk", "name", "short_description"
    list_display_links = "pk", "name"


class OrderTabularInline(admin.TabularInline):
    model = Product.orders.through


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, ShortDescriptionMixin):
    inlines = [
        OrderTabularInline,
    ]
    list_display = "pk", "title", "price", "category", "short_description"
    list_display_links = "pk", "title"


class ProductTabularInline(admin.TabularInline):
    model = Order.products.through


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ProductTabularInline,
    ]
    list_display = "pk", "address", "comment"
    list_display_links = "pk", "address", "comment"


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "order",
        "product",
        "quantity",
        "price",
    )
    list_display_links = "pk",


# @admin.register(Category, OrderProduct)
# class CommonAdmin(admin.ModelAdmin):
#     pass