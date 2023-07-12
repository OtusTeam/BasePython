from django.db.models import Q
from django.test import TestCase
from django.urls import reverse

from shop.models import Category


class TestCategoriesListTestCase(TestCase):
    # def setUp(self) -> None:

    @classmethod
    def setUpClass(cls):
        cls.category = Category.objects.create(
            name="unique-category-name",
            description="some description",
        )

    @classmethod
    def tearDownClass(cls):
        cls.category.delete()

    def test_get_category(self):
        qs = Category.objects.filter(~Q(name="default"))
        count = qs.count()
        self.assertEqual(count, 1)
        category = qs.get()
        self.assertEqual(category.pk, self.category.pk)

    def test_get_category_details(self):
        url = reverse("shop:category", kwargs={"pk": self.category.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, "shop/category_detail.html")
        self.assertContains(response, self.category.description)
        self.assertContains(response, self.category.name)
        self.assertContains(response, self.category.pk)
