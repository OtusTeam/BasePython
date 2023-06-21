from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from .models import Product


def shop_index(request: HttpRequest) -> HttpResponse:
    products = Product.objects.order_by("id").all()
    return render(
        request=request,
        template_name="shop/index.html",
        context={
            "products": products,
        },
    )
