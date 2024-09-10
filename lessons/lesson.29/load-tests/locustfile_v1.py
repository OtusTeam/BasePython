from typing import TypedDict

from locust import HttpUser, task


class UserDataType(TypedDict):
    id: int
    username: str


class UsersApiUser(HttpUser):
    USERS_API_BASE_PATH = "/api/v1/users/"

    @task
    def load_users_v1(self):
        response = self.client.get(self.USERS_API_BASE_PATH)
        users: list[UserDataType] = response.json()
        for user in users:
            user_id = user["id"]
            url = f"{self.USERS_API_BASE_PATH}{user_id}/"
            self.client.get(url)
