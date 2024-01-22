from django.test import TestCase
from animals.models import Category, Animal


class CategoryTestCase(TestCase):

    def setUp(self):
        print('Я выполняюсь перед каждым тестом')
        self.category_name = 'tiger'
        self.category = Category.objects.create(name=self.category_name)

    def tearDown(self):
        print('Я выполняюсь после каждого теста')

    def test_str(self):
        category = Category(name='tiger')
        self.assertEqual(str(category), 'tiger')

    def test_str_db(self):
        self.assertEqual(str(self.category), self.category_name)

    def test_str_animal(self):
        animal = Animal.objects.create(category=self.category, name='Boris')
        self.assertEqual(str(animal), 'Boris (tiger)')


class AnimalTestCase(TestCase):

    def test_str(self):
        category = Category.objects.create(name='tiger')
        animal = Animal.objects.create(category=category, name='Boris')
        self.assertEqual(str(animal), 'Boris (tiger)')
