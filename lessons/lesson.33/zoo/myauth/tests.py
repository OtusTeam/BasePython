from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from animals.models import AnimalKind, Animal


class TestUserAuth(TestCase):
    def setUp(self):
        # self.client = Client()
        self.user_data = {'username': 'user1',
                          'email': 'user1@otus.local',
                          'password': 'pass'}
        self.user = get_user_model().objects.create_user(
            **self.user_data
        )

    def test_user_force_login(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_anonymous)

        # logged
        self.client.login(username=self.user_data['username'],
                          password=self.user_data['password'])
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_anonymous)
        self.assertEqual(response.context['user'], self.user)

    def test_user_login_redirect(self):
        kind = AnimalKind.objects.create(name='lion', desc='strong animal')
        animal = Animal.objects.create(name='Alex', kind=kind, age=3)

        response = self.client.get(reverse('animal_detail',
                                           kwargs={'pk': animal.pk}))

        self.assertEqual(response.status_code, 302)

        # logged
        self.client.login(username=self.user_data['username'],
                          password=self.user_data['password'])

        response = self.client.get(reverse('animal_detail',
                                           kwargs={'pk': animal.pk}))
        self.assertEqual(response.status_code, 200)

    def test_user_real_login(self):
        # get
        response = self.client.get(
            '/auth/login/'
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_anonymous)
        self.assertIn('form', response.context)

        # post
        response = self.client.post(
            '/auth/login/',
            data={'username': self.user_data['username'],
                  'password': self.user_data['password']}
        )
        self.assertEqual(response.status_code, 302)

        # main page
        response = self.client.get(
            '/'
        )
        self.assertFalse(response.context['user'].is_anonymous)
        self.assertEqual(response.context['user'], self.user)
