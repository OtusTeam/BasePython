import random


def add(num_1, num_2):
    """Функция сложения."""
    return num_1 + num_2


def sub(num_1, num_2):
    """Функция вычитания."""
    return num_1 - num_2


def mul(num_1, num_2):
    """Функция умножения."""
    return num_1 * num_2


def div(num_1, num_2):
    """Функция деления."""
    if num_2 == 0:
        raise ValueError('Деление на ноль')
    return num_1 / num_2


def get_num():
    return random.randint(1, 100) + 100