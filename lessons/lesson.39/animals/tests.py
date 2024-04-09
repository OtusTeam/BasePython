from django.test import TestCase

from animals.models import Animal


# from unittest import TestCase


class AnimalsTest(TestCase):
    fixtures = ['animals.json', 'myauth.json']

    def test_animals_qty(self):
        animals_qty = Animal.objects.count()  # db level, F()
        # animals_qty = len(Animal.objects.all())  # python level
        self.assertEqual(animals_qty, 6)

    def test_main_login_required(self):
        response = self.client.get('/')
        self.assertEqual(302, response.status_code)

        # force login
        self.client.login(username='otus', password='pass')

        response = self.client.get('/')
        self.assertFalse(response.context['user'].is_anonymous)
        self.assertEqual(200, response.status_code)
