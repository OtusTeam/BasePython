from django.urls import path

from .views import ProductsIndexView, OrdersIndexView

app_name = "shop_app"

urlpatterns = [
    path("products/", ProductsIndexView.as_view(), name="products_index"),
    path("orders/", OrdersIndexView.as_view(), name="orders_index"),
]
