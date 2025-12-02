from os import getenv
from typing import TypedDict

from locust import HttpUser, task


API_PREFIX = getenv("API_PREFIX")

print("starting for api", API_PREFIX)


class UserData(TypedDict):
    id: int
    username: str


class GenericUser(HttpUser):
    users_base_url = f"{API_PREFIX}/users/"
    users_details_url = users_base_url + "{user_id}/"

    @task
    def get_users(self):
        response = self.client.get(self.users_base_url)
        users_data: list[UserData] = response.json()
        for user in users_data:
            user_id = user["id"]
            self.client.get(
                self.users_details_url.format(user_id=user_id),
                name=self.users_details_url,
            )
