from os import getenv

from locust import HttpUser, task


API_VERSION = "v1"
if version := getenv("API_VERSION"):
    API_VERSION = version

print("Starting on API version", API_VERSION)


class UserApiUser(HttpUser):
    base_url = f"/api/{API_VERSION}/users/"

    @task
    def get_users_and_details(self):
        response = self.client.get(self.base_url)

        users = response.json()
        for user in users:
            user_id = user["id"]

            self.client.get(
                f"{self.base_url}{user_id}/",
                name="/api/users/:user_id",
            )
