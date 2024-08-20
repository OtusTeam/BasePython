from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from celery.result import AsyncResult

from shop_app.models import Product, Order


class ProductsIndexView(TemplateView):
    template_name = "shop_app/products_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            # products=Product.objects.all(),
            products=(
                Product.objects.filter(archived=False).select_related("category").all()
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
                Order.objects.select_related("user")
                .prefetch_related("order_products__product")
                .all()
            ),
        )
        return context


def task_status(request: HttpRequest) -> HttpResponse:
    context = {}
    task_id = request.GET.get("task_id")
    result = AsyncResult(id=task_id)
    is_ready = result.ready()
    status = result.status
    task_result = result.result
    context.update(
        task_id=task_id,
        is_ready=is_ready,
        status=status,
        result=task_result,
    )
    return render(
        request=request,
        template_name="shop_app/task_status.html",
        context=context,
    )
