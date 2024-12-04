from step_2 import add
import pytest


@pytest.mark.parametrize("a, b, expected", [
    (4, 2, 2),
    (9, 3, 3),
    (15, 5, 3)
])
def test_add(a, b, expected):
    result = add(a, b)
    assert result == expected


@pytest.mark.parametrize("number", [1, 2, 3, 4, 5, 6, 7])
def test_positive(number):
    assert number > 0


if __name__ == '__main__':
    pytest.main()