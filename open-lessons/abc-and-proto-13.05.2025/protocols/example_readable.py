import random
import string
from typing import Protocol

FILE_PATH = "/Users/suren/MyFiles/edu/OTUS/open-lessons/pb-abc-and-proto-13.05/file.txt"


class Readable(Protocol):
    def read(self) -> bytes: ...


class ApiClient(Readable):
    def __init__(self, url: str) -> None:
        self.url = url

    def api_call(self) -> None:
        print("calling api self", self)

    def read(self) -> bytes:
        return f"reading api, {self.url}".encode()


class RandomReader:
    def read(self) -> bytes:
        line = str(self) + "".join(random.choices(string.ascii_letters, k=10))
        return line.encode()


def stream_data(filelike: Readable) -> None:
    print("streaming data", filelike.read())


def main() -> None:
    api = ApiClient("https://example.com/api-resource")

    random_reader = RandomReader()
    stream_data(api)
    stream_data(random_reader)

    with open(FILE_PATH, "rb") as file:
        stream_data(file)


if __name__ == "__main__":
    main()
