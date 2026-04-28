from django.urls import path

from shop_app import views

app_name = "shop_app"

urlpatterns = [
    path(
        "",
        views.ProductsListView.as_view(),
        name="products_list",
    ),
    path(
        "add/",
        views.ProductCreateView.as_view(),
        name="create_product",
    ),
]
