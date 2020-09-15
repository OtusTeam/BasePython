URL = "sqlite:///:memory:"

missing = object()


class User:
    GROUPS = [1, 2, 3]

    @staticmethod
    def group_exists(cls, group_id):
        """
        >>> User.group_exists(1)
        ... True
        >>> User.group_exists(4)
        ... False

        :param group_id:
        :return:
        """
        return group_id in cls.GROUPS

    def __init__(self, username):
        self.username = username

    def __str__(self):
        return self.username

    def delete(self):
        print("Deleted user", self)
        return True


class Engine:
    def __init__(self, url):
        self.url = url


class Connection:
    def __init__(self, engine):
        self.engine = engine

    def get_user(self, username):
        if username == "test":
            return missing
        return User(username)

    def get_admin(self):
        return self.get_user("admin")

    def get_user_optional(self, username, default=missing):
        # could not find user
        return default


def get_engine(url=URL):
    return Engine(url=url)


def get_connection(engine=None):
    if engine is None:
        engine = get_engine()
    return Connection(engine=engine)


def get_user(username):
    conn = get_connection()
    return conn.get_user(username)


def test_returns_missing():
    conn = get_connection()
    user = conn.get_user_optional("qweqwe")
    assert user is missing
