from typing import TypedDict

from locust import HttpUser, task


class User(TypedDict):
    id: int
    username: str


class AsyncUserApiV3(HttpUser):
    URL_API_USERS = "/api/v3/users/"

    @task
    def get_users(self):
        response = self.client.get(self.URL_API_USERS)
        users: list[User] = response.json()
        for user in users:
            user_id = user["id"]
            self.client.get(f"{self.URL_API_USERS}{user_id}/")
