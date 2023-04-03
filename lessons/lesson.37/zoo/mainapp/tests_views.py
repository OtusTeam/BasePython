from django.test import TestCase
from .models import Category, Animal
from userapp.models import MyUser


class TestViews(TestCase):

    # 1. Страница отвечает
    # 2. На страницу передаются нужные данные
    # 3. На странице есть кнопка search

    def test_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_context(self):
        category = Category.objects.create(name='Медведь')
        animal = Animal.objects.create(name='Борис', category=category)
        response = self.client.get('/')
        # print(response.context)
        self.assertTrue('animals' in response.context)
        self.assertEqual(response.context['animals'].first().id, animal.id)

    def test_content(self):
        response = self.client.get('/')
        button_element = '<button class="btn btn-outline-success" type="submit">Search</button>'

        self.assertIn(button_element, response.content.decode(encoding='utf-8'))
        self.assertIn(button_element.encode(encoding='utf-8'), response.content)

    def test_category_list_auth(self):
        response = self.client.get('/category-list/')
        self.assertEqual(response.status_code, 302)

        username = 'auth_user'
        password = 'admin123456'
        user = MyUser.objects.create_user(
            username='auth_user',
            email='auth@user.com',
            password='admin123456',
        )

        self.client.login(username=username, password=password)

        response = self.client.get('/category-list/')

        self.assertEqual(response.status_code, 200)

        self.client.logout()

        response = self.client.get('/category-list/')
        self.assertEqual(response.status_code, 302)

    def test_category_create_auth(self):
        response = self.client.get('/category-create/')
        self.assertEqual(response.status_code, 302)

        username = 'auth_user'
        password = 'admin123456'
        user = MyUser.objects.create_user(
            username=username,
            email='auth@user.com',
            password=password,
        )
        #
        self.client.login(username=username, password=password)
        #
        response = self.client.get('/category-create/')

        self.assertEqual(response.status_code, 403)
        #
        self.client.logout()
        #
        # response = self.client.get('/category-list/')
        # self.assertEqual(response.status_code, 302)
        user = MyUser.objects.create_user(
            username='staff_user',
            email='staff@user.com',
            password='admin123456',
            is_staff=True
        )

        self.client.login(username='staff_user', password='admin123456')

        response = self.client.get('/category-create/')

        self.assertEqual(response.status_code, 200)
