import os
import logging
from locust import HttpUser, task

api_version = os.getenv("API_VERSION") or "v1"

print("Starting on API", api_version)


class UsersApiUser(HttpUser):
    USERS_API = f"/api/{api_version}/users/"

    @task
    def get_users_details(self):
        response = self.client.get(self.USERS_API)
        for user in response.json():
            url = f"{self.USERS_API}{user['id']}/"
            response = self.client.get(url)
            logging.debug(response.json())
