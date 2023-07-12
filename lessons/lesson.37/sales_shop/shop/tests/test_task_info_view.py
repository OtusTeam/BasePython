from http import HTTPStatus
from typing import Type

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.test import TestCase
from django.urls import reverse

from sales_shop.fake import fake


UserModel: Type[AbstractUser] = get_user_model()


class GetTaskInfoTestCase(TestCase):
    def setUp(self) -> None:
        self.username = fake.user_name()
        self.password = fake.password()
        self.user: AbstractUser = UserModel.objects.create_user(
            username=self.username,
            password=self.password,
        )
        # self.client.login(
        #     username=self.username,
        #     password=self.password,
        # )
        # print("created user", self.user)

    def test_anon_user_no_access(self):
        # self.client.logout()
        url = reverse("shop:get-order-task", kwargs={"task_id": fake.word()})
        response = self.client.get(url)
        # self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse("site_auth:login") + f"?next={url}")

    def test_get_task_info_pending(self):
        task_id = str(fake.pyint())
        url = reverse("shop:get-order-task", kwargs={"task_id": task_id})
        self.client.login(
            username=self.username,
            password=self.password,
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertJSONEqual(
            response.content,
            # ["foo", "bar"],
            {
                "task_id": task_id,
                "status": "PENDING",
                "name": None,
            },
        )
