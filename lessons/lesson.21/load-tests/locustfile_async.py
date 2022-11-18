from typing import TypedDict

from locust import HttpUser, task

User = TypedDict("User", {"username": str, "id": int})


class HelloWorldUserSyncAPI(HttpUser):
    @task
    def hello_world(self):
        response = self.client.get("/users")
        users: list[User] = response.json()
        for user in users:
            self.client.get(f"/users/{user['id']}")
