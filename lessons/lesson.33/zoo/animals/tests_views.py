# from django.test import Client
from django.test import TestCase
from mixer.backend.django import mixer
from .models import Animal, Kind, Family
from users.models import MyUser


class TestViews(TestCase):

    def test_views(self):
        # client = Client()
        response = self.client.get('/')
        # Проверка кода ответа
        self.assertEqual(response.status_code, 200)

        # Проверка контекста
        response = self.client.get('/')
        self.assertEqual('object_list' in response.context, True)
        self.assertTrue('object_list' in response.context)
        self.assertIn('object_list', response.context)
        self.assertEqual(len(response.context['object_list']), 0)

        # Проверка контента
        response = self.client.get('/')
        # print(response.content)
        # print(type(response.content))
        self.assertIn(b'Navbar example', response.content)
        name = b'\xd0\xa1\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd1\x82\xd1\x8c'
        self.assertIn(b'\xd0\xa1\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd1\x82\xd1\x8c', response.content)
        self.assertIn('Создать'.encode(encoding='utf-8'), response.content)
        self.assertIn('Создать', response.content.decode(encoding='utf-8'))


class TestAuthAnimalCreateView(TestCase):

    def test_auth(self):
        # family = Family.objects.create(name='Тигр')
        # kind = Kind.objects.create(name='Амурский', family=family)
        # animal = Animal.objects.create(kind=kind, name='Борис')
        animal = mixer.blend(Animal)
        url = f'/animal/delete/{animal.pk}/'

        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

        login = 'admin'
        password = 'admin123456'
        user = MyUser.objects.create_superuser(username=login, email='admin@admin.com', password=password)

        self.client.login(username=login, password=password)

        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

        self.client.logout()

        login = 'toma'
        password = 'admin123456'
        user = MyUser.objects.create_superuser(username=login, email='admin1@admin1.com', password=password)

        self.client.login(username=login, password=password)

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

