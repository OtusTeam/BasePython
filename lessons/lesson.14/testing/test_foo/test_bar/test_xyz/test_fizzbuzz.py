import pytest

from foo.bar.xyz.fizzbuzz import fizzbuzz


# class TestFizzBuzz
@pytest.mark.parametrize(
    "value, expected",
    [
        (3, "Fizz"),
        (5, "Buzz"),
        (15, "FizzBuzz"),
        (10, "Buzz"),
        (2, ""),
        (7, ""),
    ],
)
def test_fizzbuzz(value: int, expected: str) -> None:
    assert fizzbuzz(value) == expected
