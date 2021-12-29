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
    user = User(str(random.randbytes(8)))
    print("created user", user)
    # return user
    yield user
    print("delete user", user)
    user.delete()


@fixture
def engine_default():
    return get_engine()


@fixture
def conn_default(engine_default):
    return get_connection(engine=engine_default)


class TestUser:

    def test_init(self):
        username = "spam_and_eggs"
        user = User(username)
        assert user.username == username

    def test_set_age(self, user):
        new_age = 42
        user.set_age(new_age)
        assert user.age == new_age

    def test_update_username(self, user):
        old_username = user.username
        new_username = str(random.randbytes(10))
        assert new_username != old_username
        user.username = new_username
        assert user.username == new_username

    def test_delete(self, user):
        assert user.delete() is True


def test_connection_default(conn_default, engine_default):
    assert conn_default.engine is engine_default
    assert isinstance(conn_default, Connection)
    assert isinstance(engine_default, Engine)


# def test_get..(conn_default):
#     conn_default...

@mock.patch("db_helper.get_engine", autospec=True)
@mock.patch("db_helper.get_connection", autospec=True)
def test_get_user(mock_get_connection, mock_get_engine, user):
    username = user.username = "sam_smith"
    # mock_get_connection(123, 3456)
    print("in test", mock_get_connection)
    # print(user)
    mocked_conn = mock_get_connection.return_value
    mocked_get_user = mocked_conn.get_user
    mocked_get_user.return_value = user

    res = get_user(username)
    assert res is user
    mocked_get_user.assert_called_once_with(username)
    mock_get_engine.assert_not_called()
