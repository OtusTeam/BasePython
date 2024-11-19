from typing import TypedDict

from locust import HttpUser, task


class AuthorData(TypedDict):
    id: int
    username: str


class ReadAuthorsUser(HttpUser):
    AUTHORS_API_URL = "/api/v1/authors/"

    @task
    def load_authors_v1(self):
        result = self.client.get(self.AUTHORS_API_URL)
        data: list[AuthorData] = result.json()
        for author in data:
            url = f"{self.AUTHORS_API_URL}{author['id']}/"
            self.client.get(url)
