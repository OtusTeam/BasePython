from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from django.utils.translation import gettext_lazy as _


class MyUserRegisterTest(TestCase):
    # fixtures = ['myauth.json']

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
        response = self.client.post(
            '/myauth/register/',
            data=self.user_data
        )
        # print(response.content.decode())
        self.assertEqual(302, response.status_code)

        new_user = get_user_model().objects.get(
            username=self.user_data['username']
        )

        self.assertEqual(self.user_data['email'],
                         new_user.email)

    def test_fail_register(self):
        response = self.client.post(
            reverse('myauth:register'),
            data=self.user_broken_data
        )
        self.assertEqual(200, response.status_code)
        self.assertFormError(
            response,
            'form',
            'password2',
            _('The two password fields didn’t match.')
            # 'Введенные пароли не совпадают.'
        )
