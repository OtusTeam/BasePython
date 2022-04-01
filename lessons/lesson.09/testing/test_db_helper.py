import random
from string import ascii_letters
from unittest import mock

from pytest import fixture

from db_helper import (
    User,
    Engine,
    Connection,
    get_engine,
    get_connection,
    get_user,
)


@fixture
def user():
    letters = random.choices(ascii_letters, k=8)
    username = "".join(letters)
    print("prepared username", username)
    return User(username)


@fixture
def engine_default():
    return get_engine()


@fixture
def conn_default(engine_default):
    return get_connection(engine=engine_default)


class TestUser:
    def test_init(self):
        username = "spam-and-eggs"
        user = User(username)
        assert user.username == username

    def test_set_age(self, user):
        age = random.randint(0, 100)
        assert user.age != age
        user.set_age(age)
        assert user.age == age

    def test_delete(self, user):
        res = user.delete()
        assert res


def test_connection_default(conn_default, engine_default):
    assert conn_default.engine is engine_default
    assert isinstance(conn_default, Connection)
    assert isinstance(engine_default, Engine)


@mock.patch("db_helper.get_connection", autospec=True)
def test_get_user(mock_get_connection, user):
    username = user.username

    print("gonna fetch user", user)
    print("mock_get_connection", mock_get_connection)
    mock_conn = mock_get_connection.return_value
    print("mock_conn", mock_conn)

    mock_conn.get_user.return_value = user

    u = get_user(username)
    assert u is user
    mock_get_connection.assert_called_once_with()
    mock_conn.get_user.assert_called_once_with(username)
