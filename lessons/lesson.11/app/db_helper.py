URL = "sqlite://:memory:"


class User:

    def __init__(self, username):
        self.username = username
        self.is_staff = False
        # self.username = "qwe"

    def __str__(self):
        return self.username

    def delete(self):
        print("deleted user", self)
        return True


class Engine:
    def __init__(self, url):
        self.url = url


class Connection:
    def __init__(self, engine: Engine):
        self.engine = engine

    def get_user(self, username):
        print("conn get username", username)
        return User(username)


def get_engine(url=URL):
    return Engine(url)


def get_connection(engine=None):
    if engine is None:
        engine = get_engine()
    return Connection(engine)


def get_user(username):
    conn = get_connection()
    return conn.get_user(username)
