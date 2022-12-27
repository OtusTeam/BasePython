from django.test import TestCase
from .models import Category, Animal
from django.contrib.auth.models import User

class TestAnimalListView(TestCase):

    def test_response_status_code(self):
        response = self.client.get('/animals/')
        self.assertEqual(response.status_code, 200)

    def test_response_context(self):
        response = self.client.get('/animals/')
        self.assertIn('help_text', response.context)
        self.assertEqual(response.context['help_text'], 'Тебе в помощь')

    def test_animal_detail(self):
        response = self.client.get('/animals/999/')
        self.assertEqual(response.status_code, 404)

        category = Category.objects.create(name='Попугай')
        animal = Animal.objects.create(name='Кеша', category=category)

        response = self.client.get(f'/animals/{animal.pk}/')
        self.assertEqual(response.status_code, 200)

    def test_content(self):
        response = self.client.get('/animals/')
        button = '<a class="btn btn-primary" href="/animals/create/">Создать</a>'.encode(encoding='utf-8')
        self.assertIn(button, response.content)

        button = '<a class="btn btn-primary" href="/animals/create/">Создать</a>'
        self.assertIn(button, response.content.decode(encoding='utf-8'))


    def test_permissions(self):
        # Это гость
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        # Создаем пользователя
        user = User.objects.create_user(username='user', email='user@email.com', password='user123456')
        user = User.objects.create_superuser(username='user', email='user@email.com', password='user123456')
        self.client.login(username='user', password='user123456')
        # Авторизованный запрос
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.client.logout()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
