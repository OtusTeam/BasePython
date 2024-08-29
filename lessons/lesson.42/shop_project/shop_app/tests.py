from django.test import TestCase

from .models import Category


class CategoryTest(TestCase):
    fixtures = [
        'category.json',
        'my_auth.json',
    ]

    def test_animals_qty(self):
        qty = Category.objects.count()  # db level, F()
        # qty = len(Category.objects.all())  # python level
        self.assertEqual(qty, 3)

    def test_orders_login_required(self):
        response = self.client.get('/shop/orders/')
        self.assertEqual(302, response.status_code)

        # force login
        self.client.login(username='otus', password='pass')

        response = self.client.get('/shop/orders/')
        self.assertEqual(200, response.status_code)
        self.assertFalse(response.context['user'].is_anonymous)
