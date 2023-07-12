from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse


class HelloViewTestCase(TestCase):
    def test_get_ok(self):
        url = reverse("shop:hello")
        response = self.client.get(url)
        self.assertHTMLEqual(response.content.decode(), "<h1>Hello View</h1>")


class ShopIndexViewTestCase(TestCase):

    def test_index_view_status_ok(self):
        url = reverse("shop:index")
        response = self.client.get(url)
        # self.assertEqual(response.status_code, 200)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        # self.assertInHTML("<h1>Shop index</h1>", response, count=1)
        self.assertTemplateUsed(response, "shop/index.html")
