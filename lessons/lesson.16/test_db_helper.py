from unittest import mock

from pytest import fixture

from db_helper import (
    User,
    Engine,
    Connection,
    get_connection,
    get_user,
)


@fixture
def user():
    print("Crete user obj")
    user = User("test_user")
    # return user
    yield user
    #
    user.delete()


class TestUser:
    def test_init(self):
        username = "adminuser"
        u = User(username)
        assert u.username == username

    def test_delete(self):
        u = User("qwe")
        res = u.delete()
        assert res is True


def test_get_connection():
    conn = get_connection()
    assert isinstance(conn, Connection)
    assert isinstance(conn.engine, Engine)


@mock.patch("db_helper.get_connection", autospec=True)
def test_get_user(mocked_get_connection, user):
    username = "username"
    mocked_conn_get_user = mocked_get_connection.return_value.get_user
    mocked_conn_get_user.return_value = user
    res = get_user(username)
    assert res is user

    # mocked_conn_get_user.assert_called()
    # mocked_conn_get_user.assert_called_once()
    mocked_conn_get_user.assert_called_once_with(username)
