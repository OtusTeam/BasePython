from django.contrib.auth.models import AbstractUser
from django.test import TestCase
from django.db import models
from django.urls import reverse

from myauth.models import UserModel


class UserLoginTestCase(TestCase):

    def setUp(self) -> None:
        # cls.user = UserModel.objects.create()
        # cls.user.set
        password = "qwerty123"
        self.user: AbstractUser = UserModel.objects.create_user(
            "john",
            "john@example.com",
            password,
        )
        self.password = password

    def test_user_login(self):
        response = self.client.post(
            reverse("login"),
            data={
                "username": self.user.username,
                "password": self.password,
            },
        )

        self.assertEqual(response.url, reverse("animals:list"))

        response = self.client.get(reverse("animals:list"))
        self.assertFalse(response.context["user"].is_anonymous)

    def test_access_to_protected_page(self):
        # self.client.post(reverse("login"))
        self.client.login(username=self.user.username, password=self.password)

        response = self.client.get(
            reverse("animals:create"),
        )
        self.assertFalse(response.context["user"].is_anonymous)

        self.assertEqual(response.status_code, 200)
