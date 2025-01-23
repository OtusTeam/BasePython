from my_module import add, divide, sub
import pytest


@pytest.mark.parametrize('a, b, expected', [
    (2, 3, 5),
    (5, 7, 12),
    (3, 5, 8)
])
def test_add(a, b, expected):
    result = add(a, b)
    assert result == expected


# def test_add1():
#     result = add(5, 7)
#     assert result == 12
#
#
# def test_add2():
#     result = add(3, 5)
#     assert result == 8


def test_sum_case(data):
    assert sum(data) == 6


def test_max_case(data):
    assert max(data) == 3


def test_devide():
    result = divide(10, 2)
    assert result == 5


def test_devide_by_zero():
    try:
        divide(10, 0)
    except ValueError as e:
        assert str(e) == 'divide by zero'

    # except ZeroDivisionError:
    #     assert True
    # result = divide(10, 0)
    # assert result == 5


def test_sub():
    result = sub(7, 4)
    assert result == 3


if __name__ == '__main__':
    pytest.main(['-v'])