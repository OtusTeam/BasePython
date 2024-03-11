from random import randint
from unittest import mock

import pytest

from db_helper import get_connection, get_engine, Engine, Connection, User, get_user


@pytest.fixture()
def url_default():
    print("call url_default")
    # return "sqlite:///:memory:"
    return object()


@pytest.fixture()
def engine_default(url_default):
    print("call engine_default")
    return get_engine(url=url_default)


@pytest.fixture()
def connection_default(engine_default):
    print("call connection_default")
    return get_connection(engine=engine_default)


def test_fixtures_are_bound(connection_default, engine_default, url_default):
    assert isinstance(connection_default, Connection)
    assert isinstance(engine_default, Engine)
    assert connection_default.engine is engine_default
    assert engine_default.url is url_default


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
