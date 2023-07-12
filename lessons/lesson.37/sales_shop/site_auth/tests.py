from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse, reverse_lazy
from typing import Type

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


UserModel: Type[AbstractUser] = get_user_model()


class LoginViewTestCase(TestCase):
    login_url = reverse_lazy("site_auth:login")

    def setUp(self) -> None:
        self.username = "user_testing"
        self.password = "supersecretpassword!23A"
        self.user: AbstractUser = UserModel.objects.create_user(
            username=self.username,
            password=self.password,
        )

    def test_login_anon(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        user = response.context["user"]
        self.assertTrue(user.is_anonymous)

    def test_login_success(self):
        response = self.client.post(
            self.login_url,
            {
                "username": self.username,
                "password": self.password,
            },
        )
        about_me_url = reverse("site_auth:about-me")
        self.assertRedirects(response, about_me_url)

        response_me = self.client.get(about_me_url)
        self.assertEqual(response_me.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response_me, "site_auth/me.html")
        user = response_me.context["user"]
        self.assertFalse(user.is_anonymous)
        self.assertEqual(user.username, self.user.username)
