URL_DEFAULT = "sqlite://"


class Engine:
    def __init__(self, url: str, echo: bool = False):
        self.url = url
        self.echo = echo


class Connection:
    def __init__(self, engine):
        self.engine = engine


def get_engine(url=None, echo: bool = False):
    return Engine(url or URL_DEFAULT)


def get_connection(engine=None):
    if engine is None:
        engine = get_engine()
    return Connection(engine)


class User:
    def __init__(self, username: str):
        self.username = username
        self.age = None

    def __str__(self):
        return self.username

    def set_age(self, age: int):
        self.age = age

    def delete(self):
        print("delete", self)
        return True
