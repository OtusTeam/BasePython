"""
Домашнее задание №1
Функции и структуры данных
"""
from typing import List


def power_numbers(*args: int):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [item * item for item in args]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num: int) -> bool:
    if num < 2:
        return False
    elif num == 2:
        return True

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def filter_numbers(numbers: List[int] = None, filter_type: str = ODD) -> List[int] | None:
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

    if filter_type not in [ODD, EVEN, PRIME]:
        return None

    if filter_type == EVEN:
        return list(filter(lambda x: x % 2 == 0, numbers))
    elif filter_type == ODD:
        return list(filter(lambda x: x % 2 != 0, numbers))
    else:
        return list(filter(lambda x: is_prime(x), numbers))
