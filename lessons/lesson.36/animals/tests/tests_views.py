from django.urls import reverse
from django.test import TestCase
from animals.models import Category
from users.models import MyUser


class AboutViewTestCase(TestCase):

    def test_status_code(self):
        url = '/animals/about/'
        response = self.client.get(url)
        print('RESPONSE', response)
        print(type(response))
        self.assertEqual(response.status_code, 200)


class CategoryViewTestCase(TestCase):

    def setUp(self):
        self.url = '/animals/categories/'

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_context(self):
        response = self.client.get(self.url)
        context = response.context
        print(type(context))
        self.assertIn('categories', context)
        categories = context['categories']
        self.assertEqual(len(categories), 0)
        tiger = Category.objects.create(name='Tiger')
        parrot = Category.objects.create(name='Parrot')
        response = self.client.get(self.url)
        context = response.context
        categories = context['categories']
        self.assertEqual(len(categories), 2)

    def test_content(self):
        # ?
        response = self.client.get(self.url)
        content: bytes = response.content
        self.assertIn(b'Categories', content)
        self.assertIn('Categories', content.decode(encoding='utf-8'))
        self.assertContains(response, 'Categories', 3)


class AnimalsIndexViewTestCast(TestCase):

    def test_status_code_guest(self):
        url = reverse('animals:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/users/login/?next=/animals/', 302)

    def test_auth(self):
        # test guest (not auth)
        url = reverse('animals:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/users/login/?next=/animals/', 302)
        username = 'fred'
        password = 'secret'
        MyUser.objects.create_user(username=username, email='user@user.com', password=password)
        self.client.login(username=username, password=password)

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        self.client.logout()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
