from os import getenv
from typing import TypedDict

from locust import HttpUser, task


API_VERSION = getenv("API_VERSION", "v1")
print("Locustfile version:", API_VERSION)


class UserData(TypedDict):
    id: int
    username: str
    email: str


class UsersApiUser(HttpUser):
    USERS_API_PATH = f"/api/{API_VERSION}/users/"

    @task
    def get_all_users(self):
        response = self.client.get(self.USERS_API_PATH)
        data: list[UserData] = response.json()
        for user in data:
            user_id = user["id"]
            user_url = f"{self.USERS_API_PATH}{user_id}/"
            self.client.get(user_url)
