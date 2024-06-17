from django.db.models import QuerySet
from django.test import TestCase
from django.urls import reverse

from animals.models import Category, Animal
from users.models import MyUser


class TestAnimalListView(TestCase):

    def setUp(self):
        self.url = '/list/'

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_context(self):
        response = self.client.get(self.url)
        self.assertIn('new_text', response.context)
        self.assertEqual('Our new text', response.context['new_text'])

        self.assertIn('object_list', response.context)

        object_list = response.context['object_list']
        self.assertTrue(isinstance(object_list, QuerySet))
        self.assertEqual(len(object_list), 0)

        self.category = Category.objects.create(
            name='Parrot'
        )
        self.animal = Animal.objects.create(
            category=self.category,
            name='John',
        )

        response = self.client.get(self.url)
        self.assertEqual(len(response.context['object_list']), 1)

    def test_content(self):
        response = self.client.get(self.url)
        # print(response.content)
        # print(type(response.content))

        self.assertIn(b'Our new text', response.content)

        self.assertIn(
            'Our new text',
            response.content.decode(encoding='utf-8'),
        )


class TestAnimalDetailView(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name='Parrot'
        )
        self.animal = Animal.objects.create(
            category=self.category,
            name='John',
        )

        self.url = reverse('animals:detail', kwargs={'pk': self.animal.pk})

    def test_auth(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)  # 404, 401, 302
        self.assertRedirects(
            response,
            f'/users/login/?next=/animal/{self.animal.pk}/',
            302,
        )
        user = MyUser.objects.create_user(
            'user',
            'user@mail.com',
            'uern383ndc',
        )
        self.client.force_login(user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
