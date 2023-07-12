from http import HTTPStatus
from typing import Type

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db.models import Q
from django.test import TestCase
from django.urls import reverse

from shop.models import Product

UserModel: Type[AbstractUser] = get_user_model()


class ProductsListViewTestCase(TestCase):
    fixtures = [
        "categories-fixture.json",
        "products-fixture.json",
    ]

    def test_ok(self):
        url = reverse("shop:products")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "shop/products.html")
        self.assertEqual(response.status_code, HTTPStatus.OK)
        products_qs = (
            Product
            .objects
            .filter(~Q(status=Product.Status.ARCHIVED))
            .order_by("id")
            .only("id")
            .all()
        )
        self.assertQuerySetEqual(
            # qs=products_qs,
            qs=products_qs,
            # qs=[product.pk for product in products_qs],
            values=(p.pk for p in response.context["products"]),
            transform=lambda p: p.pk,
            # transform=get_pk,
        )
