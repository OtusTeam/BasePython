from typing import TypedDict

from locust import HttpUser, task


class AuthorData(TypedDict):
    id: int
    name: str
    email: str


class ApiTestUser(HttpUser):
    BASE_URL = "/api/v1/authors/"

    @task
    def fetch_authors_api(self):
        response = self.client.get(self.BASE_URL)
        for author in response.json():  # type: AuthorData
            self.client.get(f"{self.BASE_URL}{author['id']}/")
