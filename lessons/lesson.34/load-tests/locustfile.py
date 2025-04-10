import os

from locust import HttpUser, task
from typing_extensions import TypedDict

API_VERSION = os.getenv("API_VERSION", "v1")

print("Locust for API version", API_VERSION)


class UserTypedDict(TypedDict):
    id: int
    username: str


class UsersApiUser(HttpUser):
    USERS_API_URL = f"/api/{API_VERSION}/users"

    @task
    def hello_world(self):
        response = self.client.get(self.USERS_API_URL)
        data: list[UserTypedDict] = response.json()
        for user in data:
            user_url = f"{self.USERS_API_URL}/{user['id']}"
            self.client.get(user_url)
