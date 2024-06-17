from django.test import TestCase
from animals.models import Category, Animal, Food


class TestCategory(TestCase):

    def test_str(self):
        category = Category.objects.create(
            name='test name'
        )
        self.assertEqual(str(category), 'Category: test name')


class TestAnimal(TestCase):

    def setUp(self):
        print('Я выполняюсь перед каждым тестом')
        self.category = Category.objects.create(
            name='Parrot'
        )
        self.animal = Animal.objects.create(
            category=self.category,
            name='John',
        )

    def tearDown(self):
        print('Я выполняюсь после каждого теста')

    def test_str(self):
        self.assertEqual(str(self.animal), f'John/Parrot')

    def test_food_count(self):
        self.assertEqual(self.animal.food_count(), 0)

        food = Food.objects.create(name='Banana')
        self.animal.food.add(food)
        self.animal.save()

        self.assertEqual(self.animal.food_count(), 1)

    def test_math(self):
        from math import sin
        self.assertEqual(sin(0), 0)
        # self.assertEqual(sin(90), 1)
