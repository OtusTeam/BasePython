from src.calculator import add, subtract, multiply, divide
import pytest


@pytest.fixture
def num():
    return 50


@pytest.fixture
def num2():
    return 5

# def test_add():
#     result = add(2, 3)
#     assert result == 5
#
#     result = add(3, 4)
#     assert result == 7


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (2, 3, 5),
        (7, 8, 15),
        (-1, -8, -9),
        (0, 0, 0)
    ]
)
def test_add(a, b, expected):
    result = add(a, b)
    assert result == expected


def test_subtract(numbers, num2):
    result = subtract(numbers[0], numbers[1])
    # numbers[0] = 100
    assert result == num2


def test_multiply(numbers, num):
    result = multiply(numbers[0], numbers[1])
    assert result == num


def test_divide():
    assert divide(8, 2) == 4
    # assert True


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        divide(10, 0)

    assert "Деление на ноль запрещено" in str(e.value)


if __name__ == '__main__':
    pytest.main(["-vv"])