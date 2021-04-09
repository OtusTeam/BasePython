from unittest import mock
from pytest import fixture
from app.db_helper import User, get_connection, get_user, Engine, Connection


@fixture
def user():
    print("Create user obj")
    user = User("test_user")
    # return user
    yield user
    user.delete()


@fixture
def admin_user():
    print("Create admin user obj")
    admin_user = User("test_admin_user")
    admin_user.is_staff = True
    return admin_user


class TestUser:
    def test_init(self):
        username = "admin"
        user = User(username)
        assert user.username == username

    def test_init_qwe(self):
        username = "qwe"
        user = User(username)
        assert user.username == username

    def test_delete(self, user):
        res = user.delete()
        assert res is True

    def test_update_username(self, user):
        new_username = "abc"
        assert user.username != new_username
        user.username = new_username
        assert user.username == new_username


def test_get_connection():
    conn = get_connection()
    assert isinstance(conn, Connection)
    assert isinstance(conn.engine, Engine)


@mock.patch("app.db_helper.get_connection", autospec=True)
def test_get_user(mocked_get_connection, user):
    username = "abcqwe"
    mocked_conn = mocked_get_connection.return_value
    print("mocked_conn", mocked_conn)
    mocked_conn_get_user = mocked_conn.get_user
    print("mocked_conn_get_user", mocked_conn_get_user)
    mocked_conn_get_user.return_value = user

    res = get_user(username)
    assert res is user

    mocked_get_connection.assert_called()
    # mocked_conn_get_user.assert_called()
    # mocked_conn_get_user.assert_called_once()
    mocked_conn_get_user.assert_called_once_with(username)
