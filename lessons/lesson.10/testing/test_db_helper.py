import random
import string
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
def user() -> User:
    letters = random.choices(string.ascii_lowercase, k=8)
    username = "".join(letters)
    print("created username", username)
    return User(username)


@fixture
def engine_default() -> Engine:
    return get_engine()


@fixture
def connection_default(engine_default) -> Connection:
    return get_connection(engine_default)


class TestUser:
    def test__init(self):
        username = "qwerty"
        u = User(username)
        assert u.username == username
        assert u.age is None

    def test_set_age(self, user):
        age = user.age
        new_age = 25
        user.set_age(new_age)
        assert user.age == new_age
        assert new_age != age

    def test_delete(self, user):
        assert user.delete()


def test_connection_default(connection_default, engine_default):
    assert connection_default.engine is engine_default
    assert isinstance(connection_default, Connection)
    assert isinstance(engine_default, Engine)


@mock.patch("db_helper.get_connection", autospec=True)
def test_get_user(mocked_get_connection, user):

    mock_conn = mocked_get_connection.return_value
    mock_conn.get_user.return_value = user

    username = user.username
    u = get_user(username)

    assert u is user

    mocked_get_connection.assert_called_once_with()
    mock_conn.get_user.assert_called_once_with(username)
