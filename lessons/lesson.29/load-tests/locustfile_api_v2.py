from typing import TypedDict

from locust import HttpUser, task


class UserData(TypedDict):
    id: int
    username: str


class HelloWorldUser(HttpUser):
    USERS_API_BASE = "/api/v2/users/"

    @task
    def load_users_v2(self):
        response = self.client.get(self.USERS_API_BASE)
        users: list[UserData] = response.json()
        for user in users:
            user_id = user["id"]
            url = f"{self.USERS_API_BASE}{user_id}/"
            self.client.get(url)
