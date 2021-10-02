# from django.test import Client
from django.contrib.auth import get_user_model
from django.test import TestCase

from animals.models import Animal, AnimalKind


class TestAnimals(TestCase):
    def setUp(self):
        # self.client = Client()
        print('setUp')

    def test_animals_empty_list(self):
        response = self.client.get('/')

        content = response.content.decode('utf-8')
        self.assertEqual(response.status_code, 200)
        # self.assertEqual('вход' in content, True)
        # self.assertTrue('вход' in content)
        self.assertIn('вход', content)
        self.assertIn('object_list', response.context)
        self.assertEqual(len(response.context['object_list']), 0)
        # print(content)
        # print(response.context)

    def test_animals_list(self):
        kind = AnimalKind.objects.create(name='lion', desc='strong animal')
        animal = Animal.objects.create(name='Alex', kind=kind, age=3)

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), 1)
        self.assertIn(animal, response.context['object_list'])


class TestAnimalsViewsPermissions(TestCase):
    super_user_data = {'username': 'otus',
                       'email': 'otus@otus.local',
                       'password': 'pass'}
    user_data = {'username': 'user1',
                 'email': 'user1@otus.local',
                 'password': 'pass'}

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.super_user = get_user_model().objects.create_superuser(
            **cls.super_user_data
        )
        cls.user = get_user_model().objects.create_user(
            **cls.user_data
        )

    def test_super_user_perm(self):
        # not logged
        response = self.client.get('/food/')
        self.assertEqual(response.status_code, 302)

        # logged as user
        self.client.login(username=self.user_data['username'],
                          password=self.user_data['password'])
        response = self.client.get('/food/')
        self.assertEqual(response.status_code, 302)

        # logged as super_user
        self.client.login(username=self.super_user_data['username'],
                          password=self.super_user_data['password'])
        response = self.client.get('/food/')
        self.assertEqual(response.status_code, 200)

    def test_delete_animal_perm(self):
        from django.contrib.auth.models import Permission

        # print(Permission.objects.all())
        # print(Permission.objects.all().values_list('name', flat=True))
        # print(Permission.objects.filter(name='Can delete animal'))
        print(self.user.user_permissions.all())
        self.user.user_permissions.add(
            Permission.objects.filter(name='Can delete animal').first()
        )
        print(self.user.user_permissions.all())
