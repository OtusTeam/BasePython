from typing import TypedDict

from locust import HttpUser, task


class User(TypedDict):
    id: int
    username: str


class UserApiV2(HttpUser):
    USERS_API = "/api/v2/users/"

    @task
    def get_users(self):
        response = self.client.get(self.USERS_API)
        users: list[User] = response.json()
        for user in users:
            user_id = user["id"]
            self.client.get(f"{self.USERS_API}{user_id}/")
