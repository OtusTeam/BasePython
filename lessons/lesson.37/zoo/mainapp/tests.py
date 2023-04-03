from django.test import TestCase
from .models import Food, Category


class TestFood(TestCase):

    def setUp(self):
        self.food = Food.objects.create(name='Банан')
        print('Я выполняюсь перед каждым тестом')

    def tearDown(self):
        print('Я выполняюсь после каждого теста')

    def test_init(self):
        self.assertEqual(self.food.name, 'Банан')

    def test_str(self):
        self.assertEqual(str(self.food), 'Банан')


class TestCategory(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Медведь')

    def test_count_category_types(self):
        names = ['банан', 'мёд']
        for name in names:
            food = Food.objects.create(name=name)
            self.category.foods.add(food)
        self.category.save()
        self.assertEqual(self.category.count_category_types(), 2)

    def test_some_error(self):
        with self.assertRaises(ValueError):
            self.category.some_error()
