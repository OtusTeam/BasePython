from pytest import fixture
from unittest import mock
from db_helper import User, Engine, Connection, get_connection, get_user


@fixture
def user():
    print("Get user fixture")
    user = User("test_user")
    yield user
    user.delete()


class TestUser:
    def test_init(self):
        username = "username"
        user = User(username)
        assert user.username == username


def test_get_connection():
    conn = get_connection()
    assert isinstance(conn, Connection)
    assert isinstance(conn.engine, Engine)


@mock.patch("db_helper.get_connection")
def test_get_user(mocked_get_connection, user):
    username = "username"
    mocked_conn_get_user = mocked_get_connection.return_value.get_user
    # expected_result = mocked_conn_get_user.return_value
    expected_result = user
    mocked_conn_get_user.return_value = expected_result
    res = get_user(username=username)
    assert res is expected_result
    # mocked_conn_get_user.assert_called()
    # mocked_conn_get_user.assert_called_once()
    mocked_conn_get_user.assert_called_once_with(username)

# get raw posts:
# get api/posts
# mocked_get_posts.return_value = [{
#     "id": 1,
#     "title": "Title",
# }]
