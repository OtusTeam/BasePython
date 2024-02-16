from typing import TypedDict

from locust import HttpUser, task


class User(TypedDict):
    id: int
    username: str


class UsersApiV2User(HttpUser):
    USERS_API_BASE = "/v2/users"

    @task
    def hello_world(self):
        response = self.client.get(f"{self.USERS_API_BASE}/all/")
        users: list[User] = response.json()
        for user in users:
            user_id = user["id"]
            self.client.get(f"{self.USERS_API_BASE}/{user_id}/")


# 100
# 100 * 60 = 6000
# 1200 users
# 6000 / 1200 = 5 user click per minute
# 24 * 1200  == 28.800
