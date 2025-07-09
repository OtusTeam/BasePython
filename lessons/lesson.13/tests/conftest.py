import pytest


# @pytest.fixture
# def numbers():
#     a = 10
#     b = 5
#     return [a, b]

#
# @pytest.fixture(scope="function")
# def numbers():
#     a = 10
#     b = 5
#     return [a, b]


@pytest.fixture(scope="module")
def numbers():
    a = 10
    b = 5
    yield [a, b]
    # import os
    # os.remove("text.txt")
    print('123')