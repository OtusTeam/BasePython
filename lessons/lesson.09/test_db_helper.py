import random
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
    user = User(str(random.randbytes(10)))
    print("created user", user)
    yield user
    print("deleting user", user)
    user.delete()


@fixture(scope="module")
def engine_default():
    return get_engine()


@fixture(scope="module")
def conn_default(engine_default):
    return get_connection(engine_default)


class TestUser:
    def test_init(self):
        username = "qwerty"
        user = User(username)
        assert user.username == username

    def test_delete(self, user):
        assert user.delete() is True

    def test_update_username(self, user):
        old_username = user.username
        user.username += "qweqwr"

        assert user.username != old_username


def test_connection(conn_default):
    assert isinstance(conn_default, Connection)
    assert isinstance(conn_default.engine, Engine)


def test_demo_multiple_fixtures(conn_default, engine_default):
    assert conn_default.engine is engine_default


@mock.patch("db_helper.get_connection", autospec=True)
def test_get_user(mocked_get_connection, user):
    username = user.username

    print("mocked_get_connection", mocked_get_connection)
    mocked_conn = mocked_get_connection.return_value
    print("mocked_conn", mocked_conn)
    mocked_conn_get_user = mocked_conn.get_user
    print("mocked_conn_get_user", mocked_conn_get_user)
    mocked_conn_get_user.return_value = user

    res = get_user(username)
    assert res is user
    # mocked_get_connection.assert_called()
    # mocked_get_connection.assert_called_once()
    mocked_get_connection.assert_called_once_with()
