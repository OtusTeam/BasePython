from django.contrib import admin

from .models import Category
from .models import Product
from .models import Order
from .models import OrderPaymentDetails


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = "id", "name", "price", "updated_at"
    list_display_links = "id", "name"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "id", "name", "description"
    list_display_links = "id", "name"


class PaymentDetailsInline(admin.TabularInline):
    model = OrderPaymentDetails


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        PaymentDetailsInline,
    ]
    list_display = "id", "address", "user", "promocode", "created_at"
    list_display_links = "id", "promocode"

    # fields = (
    #     "id",
    #     "address",
    #     "user",
    #     "promocode",
    #     # "created_at",
    #     "payment_details",
    # )


@admin.register(OrderPaymentDetails)
class OrderPaymentDetailsAdmin(admin.ModelAdmin):
    list_display = "id", "payed_at", "card_ends_with", "status", "order"
    list_display_links = "id", "status"
