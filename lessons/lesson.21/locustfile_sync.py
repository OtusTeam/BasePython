from locust import HttpUser, task


class HelloWorldUser(HttpUser):

    @task
    def get_users_async(self):
        response = self.client.get("/users/sync")
        users: list[dict] = response.json()
        for user in users:
            self.client.get(f"/users/sync/{user['id']}")
