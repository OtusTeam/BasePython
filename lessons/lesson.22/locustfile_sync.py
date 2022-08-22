from locust import HttpUser, task


class HelloWorldUser(HttpUser):

    @task
    def get_users_sync(self):
        response = self.client.get("/sync/users")
        users: list[dict] = response.json()
        for user in users:
            self.client.get(f"/sync/users/{user['id']}")
