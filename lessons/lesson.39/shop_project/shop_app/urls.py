from django.urls import path

from .views import ProductsIndexView, OrdersIndexView, task_status

app_name = "shop_app"

urlpatterns = [
    path("products/", ProductsIndexView.as_view(), name="products_index"),
    path("orders/", OrdersIndexView.as_view(), name="orders_index"),
    path("task_status/", task_status, name="task_status"),
]
