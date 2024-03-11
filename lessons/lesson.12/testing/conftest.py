from random import choices
from string import ascii_letters

import pytest

from db_helper import User


@pytest.fixture()
def user() -> User:
    username = "".join(choices(ascii_letters, k=8))
    user = User(username=username)
    print("created user", user)
    yield user
    user.delete()


# default_db_url = ""
