import pytest
from src.my_math import add, sub, gen_rand


@pytest.fixture
def number1():
    return 3


@pytest.fixture
def number2(number1):
    return 4 + number1


@pytest.mark.parametrize('a, b, expected', [
    (1, 2, 3),
    (-1, -4, -5),
    (0, 7, 7),
    (2, 15, 17),
])
def test_add(a, b, expected):
    assert add(a, b) == expected


def test_sub(number1, number2, numbers):
    # assert sub(1, 2) == -1
    # assert sub(-1, -4) == 3
    # assert sub(17, 7) == 10
    assert sub(number2, number1) == 4
    assert sub(numbers[0], numbers[1]) == numbers[2]
    numbers[0] = 100
    numbers[1] = 30
    numbers[2] = 70
    assert sub(numbers[0], numbers[1]) == 70


def test_sub_fix(numbers):
    assert sub(numbers[0], numbers[1]) == 20


def test_get_rand(mocker):
    mocker.patch('random.randint', return_value=7)
    assert gen_rand(1, 100) == 'Число 7'