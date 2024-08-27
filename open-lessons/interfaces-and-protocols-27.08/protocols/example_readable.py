from typing import Protocol


class Readable(Protocol):
    def read(self) -> bytes: ...


class FileReader:
    def __init__(self, filename: str):
        self.filename = filename

    def read(self) -> bytes:
        """
        Тут мы читаем файл
        """
        print("reading file", self.filename)
        return self.filename.encode()


class APIReader:
    def __init__(self, api_path: str):
        self.api_path = api_path

    def read(self) -> bytes:
        """
        Тут мы читаем внешний API
        """
        print("reading api path", self.api_path)
        return self.api_path.encode()


def read_data_to_db(readable: Readable):
    print("save to db data:", readable.read())


def main():
    file_reader = FileReader("some-filename.txt")
    api_reader = APIReader("some/api/path")
    file = open(
        "/Users/suren/MyFiles/OTUS/lessons/open-lessons/py-basic-proto-and-interfaces-27.08.2024/file.txt",
        mode="rb",
    )
    read_data_to_db(file_reader)
    read_data_to_db(api_reader)
    read_data_to_db(file)


if __name__ == "__main__":
    main()
