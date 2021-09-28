import random
from unittest import mock

from pytest import fixture

from db_helper import User, get_engine, get_connection, Engine, Connection, get_user


@fixture
def user():
    user = User(str(random.randbytes(8)))
    print("created user", user)
    yield user
    print("delete user", user)
    user.delete()


@fixture(scope="module")
def engine_default():
    return get_engine()


@fixture(scope="module")
def connection_default(engine_default):
    return get_connection(engine_default)


class TestUser:
    def test_init(self):
        username = "spameegs"
        user = User(username)
        assert user.username == username

    def test_delete(self, user):
        assert user.delete() is True

    def test_update_username(self, user):
        old_username = user.username
        user.username = "qwe"

        assert user.username != old_username

    def test_user_set_age(self, user):
        new_age = 23
        user.set_age(new_age)
        assert user.age == new_age


def test_connection(connection_default):
    assert isinstance(connection_default, Connection)
    assert isinstance(connection_default.engine, Engine)


def test_multiple_fixture_reference(connection_default, engine_default):
    assert connection_default.engine is engine_default


@mock.patch("db_helper.get_engine", autospec=True)
@mock.patch("db_helper.get_connection", autospec=True)
def test_get_user(mock_get_connection, mock_get_engine, user):
    username = user.username
    print("mock_get_connection", mock_get_connection)
    mock_conn = mock_get_connection.return_value
    print("mock_conn", mock_conn)
    print("mock_conn.get_user", mock_conn.get_user)
    mock_conn.get_user.return_value = user

    res = get_user(username)
    assert res is user
    mock_conn.get_user.assert_called_once_with(username)
    mock_get_engine.assert_not_called()
