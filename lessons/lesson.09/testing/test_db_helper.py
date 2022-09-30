from string import ascii_lowercase
from random import choices, randint, choice

import pytest

from db_helper import (
    Engine,
    Connection,
    get_engine,
    get_connection,
    User,
)


"""
- User
- NotificationSettings
- NotificationSubscription

User.id <=> NotificationSettings.user_id
NotificationSubscription.settings_id <=> NotificationSettings.id

- create User (with profile)
- create NotificationSettings (for user)
- create NotificationSubscription (for NotificationSettings)
"""


@pytest.fixture(params=[
    pytest.param("url1"),
    pytest.param("url2"),
])
def conn_url(request):
    url = "-".join((request.param, choice(ascii_lowercase)))
    # print("generated conn_url", url)
    return url


@pytest.fixture(params=[
    pytest.param(True, id="echo-True"),
    pytest.param(False, id="echo-False"),
])
def engine_default(request, conn_url) -> Engine:
    # print("engine used conn_url", conn_url)
    return get_engine(url=conn_url, echo=request.param)


@pytest.fixture
def connection_default(engine_default) -> Connection:
    return get_connection(engine_default)


def test_fixtures_connection(
    connection_default,
    engine_default,
    conn_url,
):
    assert isinstance(connection_default, Connection)
    assert isinstance(engine_default, Engine)
    assert connection_default.engine is engine_default
    assert engine_default.url == conn_url
    # print("received conn_url", conn_url)


@pytest.fixture
def user():
    username = "".join(choices(ascii_lowercase, k=8))
    user = User(username)
    print("created user", user)
    yield user

    user.delete()


class TestUser:
    def test_set_age(self, user):
        age = randint(1, 100)
        assert user.age != age
        user.set_age(age)
        assert user.age == age
