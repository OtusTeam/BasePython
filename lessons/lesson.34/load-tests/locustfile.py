from os import getenv
from typing import TypedDict

from locust import HttpUser, task

API_VERSION = getenv("API_VERSION", "v1")
print("Locustfile API version", API_VERSION)


class UserTypedDict(TypedDict):
    id: int
    username: str


class UsersApiUser(HttpUser):
    USERS_API_PATH = f"/api/{API_VERSION}/users/"

    @task
    def hello_world(self):
        response = self.client.get(self.USERS_API_PATH)
        data: list[UserTypedDict] = response.json()
        for user in data:
            user_url = f"{self.USERS_API_PATH}{user['id']}/"
            self.client.get(user_url)
