from typing import Literal


def fizzbuzz(num: int) -> Literal["Fizz", "Buzz", "FizzBuzz", ""]:
    """
    >>> fizzbuzz(5)
    'Buzz'
    >>> fizzbuzz(10)
    'Buzz'
    >>> fizzbuzz(3)
    'Fizz'
    >>> fizzbuzz(15)
    'FizzBuzz'
    >>> fizzbuzz(2)
    ''
    >>> fizzbuzz('fff')
    Traceback (most recent call last):
        ...
    TypeError: not all arguments converted during string formatting
    """
    if not num % 3 and not num % 5:
        return "FizzBuzz"
    if not num % 3:
        return "Fizz"
    if not num % 5:
        return "Buzz"
    return ""
