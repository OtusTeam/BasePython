import logging
from os import getenv

from locust import HttpUser, task

log = logging.getLogger(__name__)

API_VERSION = "v1"
if version := getenv("API_VERSION"):
    API_VERSION = version

print("starting tests on api version", API_VERSION)

port = 8000 + int(API_VERSION.lstrip("v"))


class UsersApiUser(HttpUser):
    host = f"http://0.0.0.0:{port}"

    base_url = f"/api/{API_VERSION}/users/"

    @task
    def get_users_and_details(self):
        response = self.client.get(self.base_url)
        users = response.json()

        for user in users:
            user_id = user["id"]

            url = f"{self.base_url}{user_id}/"

            user_data_response = self.client.get(
                url=url,
                name="/users/:user-id",
            )
            log.debug(
                "User %s data: %s",
                user,
                user_data_response.json(),
            )
