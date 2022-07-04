URL = "sqlite:///:memory:"


class User:
    def __init__(self, username: str):
        self.username = username
        self.age = None

    def __str__(self):
        return self.username

    def set_age(self, age: int):
        print("set age", age)
        self.age = age

    def delete(self):
        print("deleted user", self)
        return True


class Engine:
    def __init__(self, url: str):
        self.url = url

    def init_connection(self):
        ...

    def destroy_connection(self):
        ...


# class EnginePG(Engine):
#     def init_connection(self):
#         pg....

class Connection:
    def __init__(self, engine: Engine):
        self.engine = engine

    def init_conn(self):
        self.engine.init_connection()

    def get_user(self, username: str):
        print("conn", self, "find user", username)
        return User(username)


def get_engine(url: str = URL):
    return Engine(url=url)


def get_connection(engine=None):
    if engine is None:
        engine = get_engine()
    return Connection(engine=engine)


def get_user(username: str):
    # print("in get user", get_connection, get_connection.__class__.mro())
    conn = get_connection()
    # print(conn)
    # print("conn", conn)
    return conn.get_user(username)
