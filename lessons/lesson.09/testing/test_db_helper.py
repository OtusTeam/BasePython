from string import ascii_letters
from random import randint, choices
from unittest import mock

from pytest import fixture

from db_helper import (
    User,
    get_engine,
    get_connection,
    get_user,
    Engine,
    Connection,
)


@fixture()
def user() -> User:
    username = "".join(choices(ascii_letters, k=8))
    user = User(username=username)
    print("created user", user)
    yield user
    user.delete()


@fixture()
def url_default():
    # random string!
    return object()


@fixture()
def engine_default(url_default):
    return get_engine(url=url_default)


@fixture()
def connection_default(engine_default):
    return get_connection(engine=engine_default)


def test_fixtures_connection(
    url_default,
    engine_default,
    connection_default,
):
    assert isinstance(engine_default, Engine)
    assert isinstance(connection_default, Connection)
    assert engine_default.url is url_default
    assert connection_default.engine is engine_default


class TestUser:

    def test_set_age(self, user: User):
        some_age = randint(1, 99)
        assert user.age != some_age
        user.set_age(some_age)
        assert user.age == some_age


@mock.patch("db_helper.get_connection", autospec=True)
def test_get_user(mocked_get_connection, user):

    mock_conn = mocked_get_connection.return_value
    mock_conn.get_user.return_value = user

    username = user.username
    u = get_user(username)

    assert u is user

    mocked_get_connection.assert_called_once_with()
    mock_conn.get_user.assert_called_once_with(username)
