import pytest


# def test_sum_case_1():
#     data = [1, 2, 3, 4, 5]
#     assert sum(data) == 15
#
#
# def test_sum_case_2():
#     data = [7, 8, 9, 10, 11]
#     assert sum(data) == 45
#

@pytest.fixture
def data():
    return [1, 2, 3, 4, 5]


# def test_sum_case_3(data):
#     data.append(6)
#     assert sum(data) == 21


def test_sum_case_4(data):
    data.pop()
    assert sum(data) == 10


def test_sum_case_5(data):
    data.append(6)
    assert sum(data) == 21