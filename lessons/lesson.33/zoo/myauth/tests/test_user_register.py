from django.contrib.auth.models import AbstractUser
from django.test import TestCase
from django.urls import reverse

from django.utils.translation import gettext_lazy as _
from myauth.models import UserModel
from myauth.forms import UserCreationForm


class UserRegisterTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user_reg_data = {
            "username": "john",
            "email": "john@example.com",
            "password1": "12345678otus",
            "password2": "12345678otus",
        }

        cls.user_reg_data_invalid_pass = {
            "username": "john",
            "email": "john@example.com",
            "password1": "12345678otus",
            "password2": "12345678otus1",
        }

    def test_user_register_success(self):
        response = self.client.post(
            reverse("user-register"),
            data=self.user_reg_data,
        )
        # self.assertEqual(302, response.status_code)
        self.assertEqual(response.status_code, 302)
        self.assertURLEqual(response.url, reverse("animals:list"))

        user: AbstractUser = UserModel.objects.get(username=self.user_reg_data["username"])
        self.assertEqual(user.email, self.user_reg_data["email"])

    def test_user_register_username_exists_error(self):
        response = self.client.post(
            reverse("user-register"),
            data=self.user_reg_data,
        )
        # self.assertEqual(302, response.status_code)
        self.assertEqual(response.status_code, 302)

        response = self.client.post(
            reverse("user-register"),
            data=self.user_reg_data,
        )
        # self.assertEqual(302, response.status_code)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(
            response,
            "form",
            "username",
            _("A user with that username already exists."),
            # "A user with that username already exists.",
        )

    def test_user_register_password_doesnt_match(self):
        response = self.client.post(
            reverse("user-register"),
            data=self.user_reg_data_invalid_pass,
        )
        self.assertEqual(response.status_code, 200)
        self.assertFormError(
            response,
            "form",
            "password2",
            UserCreationForm.error_messages["password_mismatch"],
        )
