from django.test import TestCase

from main.models import Animal


# from unittest import TestCase


class AnimalsTest(TestCase):
    fixtures = ['main.json', 'myauth.json']

    def test_animals_qty(self):
        animals_qty = Animal.objects.count()  # db level, F()
        # animals_qty = len(Animal.objects.all())  # python level
        self.assertEqual(animals_qty, 1)

    def test_main_login_required(self):
        response = self.client.get('/')
        self.assertEqual(302, response.status_code)

        self.client.login(username='otus', password='pass')
        response = self.client.get('/')  # force login
        self.assertFalse(response.context['user'].is_anonymous)
        self.assertEqual(200, response.status_code)
