from locust import HttpUser, task


class AsyncTestUser(HttpUser):

    @task
    def get_users_async(self):
        self.client.get("/users")
