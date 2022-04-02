from django.test import TestCase

from animals.models import Animal


class AnimalsTest(TestCase):
    fixtures = ['animals.json', 'myauth.json']

    def test_animals_qty(self):
        animals_qty = Animal.objects.count()
        self.assertEqual(animals_qty, 2)

    def test_main_login_required(self):
        response = self.client.get('/')
        self.assertEqual(302, response.status_code)

        self.client.login(username='user1', password='OtusOtus')
        response = self.client.get('/')  # force login
        self.assertFalse(response.context['user'].is_anonymous)
        self.assertEqual(200, response.status_code)

    def test_main_login_required_again(self):
        response = self.client.get('/')
        self.assertEqual(302, response.status_code)
