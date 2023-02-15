from typing import TypedDict

from locust import HttpUser, task

User = TypedDict("User", {"username": str, "id": int})


class UsersApiAsyncUser(HttpUser):
    API_PREFIX = "/users"

    @task
    def hello_world(self):
        response = self.client.get(self.API_PREFIX)
        users: list[User] = response.json()
        for user in users:
            user_id = user["id"]
            self.client.get(f"{self.API_PREFIX}/{user_id}")
