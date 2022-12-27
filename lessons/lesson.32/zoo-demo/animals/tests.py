from django.test import TestCase
from .models import Category, Animal, Card
import time

# Create your tests here.
class TestCategory(TestCase):


    def setUp(self) -> None:
        self.category = Category.objects.create(name='Попугай')
        print('Я выполняюсь ПЕРЕД каждым тестом')

    def tearDown(self) -> None:
        print('Я выполняюсь ПОСЛЕ каждого теста')

    def test_init(self):
        self.assertTrue(isinstance(self.category.name, str))
        self.assertEqual(self.category.name, 'Попугай')

    def test_wrong(self):
        category = Category.objects.create(name=12345)
        self.assertEqual(category.name, 12345)

    def test_str(self):
        category = Category.objects.get(name='Попугай')
        # assert str(category) == 'Попугай', 'Должно быть название ...'
        self.assertEqual(str(category), 'Попугай')

    def test_exception_method(self):
        with self.assertRaises(NotImplementedError):
            self.category.exception_method()


class TestAnimal(TestCase):

    def test_str(self):
        print('SLEEP')
        time.sleep(120)
        category = Category.objects.create(name='Попугай')
        animal = Animal.objects.create(name='Кеша', category=category)
        self.assertEqual(str(animal), 'Кеша')


class TestCard(TestCase):

    def test_bigger_phone_number(self):
        category = Category.objects.create(name='Попугай')
        animal = Animal.objects.create(name='Кеша', category=category)
        # print('ТУТ ДОЛЖНА БЫТЬ ОШИБКА')
        # with self.assertRaises(Exception):
        #     card = Card.objects.create(animal=animal, phone_number='1234567891011')
        #     print(card.phone_number)
        #     print(card)