from typing import TypedDict
from locust import HttpUser, task


class UserData(TypedDict):
    id: int
    username: str


class UsersApiV2User(HttpUser):
    USERS_API_BASE = "/api/v2/users"

    @task
    def users_api(self):
        response = self.client.get(self.USERS_API_BASE)
        users: list[UserData] = response.json()
        for user in users:
            user_id = user["id"]
            url = f"{self.USERS_API_BASE}/{user_id}"
            self.client.get(url)
