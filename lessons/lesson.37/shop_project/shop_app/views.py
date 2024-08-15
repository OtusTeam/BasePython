from django.views.generic import TemplateView

from shop_app.models import Product, Order


class ProductsIndexView(TemplateView):
    template_name = "shop_app/products_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            # products=Product.objects.all(),
            products=(
                Product.objects
                .filter(archived=False)
                .select_related("category")
                .all()
            ),
        )
        return context


class OrdersIndexView(TemplateView):
    template_name = "shop_app/orders_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            # orders=Order.objects.all(),
            # orders=Order.objects.prefetch_related("products").all(),
            # orders=Order.objects.prefetch_related("order_products").all(),
            # orders=Order.objects.prefetch_related("order_products__product").all(),
            # orders=Order.objects.select_related("user").all(),
            orders=(
                Order.objects
                .select_related("user")
                .prefetch_related("order_products__product")
                .all()
            ),
        )
        return context
