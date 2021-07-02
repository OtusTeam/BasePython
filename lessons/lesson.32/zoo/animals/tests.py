from django.test import TestCase
import math
from .models import Family, Kind, Food


class TestMath(TestCase):

    def test_sqrt(self):
        self.assertEqual(math.sqrt(4), 2)
        # assert math.sqrt(4) == 2


class TestFamily(TestCase):

    def setUp(self):
        print('Я выполняюсь перед каждый тестом')
        self.family = Family.objects.create(name='Тигр')
        self.id = self.family.id

    def tearDown(self):
        print('Я выполняюсь после каждого теста')

    def test_create(self):
        self.assertEqual(self.family.name, 'Тигр')

    def test_str(self):
        self.assertEqual(str(self.family), 'Тигр')
        family = Family.objects.get(id=self.id)
        self.assertEqual(str(family), 'Тигр')

    def test_get_some_error(self):
        with self.assertRaises(ValueError):
            self.family.get_some_error(5)


class TestFood(TestCase):

    def test_kinds_count_empty(self):
        food = Food.objects.create(name='Мёд')
        self.assertEqual(food.kinds_count(), 0)

    def test_kinds_count(self):
        food = Food.objects.create(name='Мёд')
        family = Family.objects.create(name='Тигр')
        kind = Kind.objects.create(name='Амурский', family=family)
        food.kinds.add(kind)
        food.save()
        self.assertEqual(food.kinds_count(), 1)
