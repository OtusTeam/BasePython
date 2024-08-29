from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class ShopUserRegisterTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user_data = {
            'username': 'otus',
            'email': 'admin@otus.local',
            'password1': 'OtusOtus',
            'password2': 'OtusOtus',
        }
        cls.user_broken_data = {
            'username': 'otus',
            'email': 'admin@otus.local',
            'password1': 'OtusOtus',
            'password2': 'Otus',
        }

    def test_succ_register(self):
        response = self.client.get(
            '/auth/register/',
            # reverse('my_auth:register'),
        )
        # self.assertIn('Username:', response.content.decode())
        self.assertContains(response, 'Username:', status_code=200)
        # self.assertEqual(200, response.status_code)

        # # post
        response = self.client.post(
            '/auth/register/',
            data=self.user_data,
        )

        self.assertEqual(302, response.status_code)

        # check user
        new_user = get_user_model().objects.get(
            username=self.user_data['username']
        )

        self.assertEqual(
            self.user_data['email'],
            new_user.email,
        )

    def test_fail_register(self):
        response = self.client.post(
            # reverse('my_auth:register'),
            '/auth/register/',
            data=self.user_broken_data,
        )
        self.assertEqual(200, response.status_code)

        self.assertFormError(
            response.context['form'],
            'password2',
            ['The two password fields didn’t match.']
            # _('The two password fields didn’t match.')
            # 'Введенные пароли не совпадают.'
        )
