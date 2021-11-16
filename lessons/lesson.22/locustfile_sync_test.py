from locust import HttpUser, task


class SyncTestUser(HttpUser):

    @task
    def get_users_sync(self):
        self.client.get("/users/sync/")
