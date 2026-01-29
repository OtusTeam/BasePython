import random


def add(a, b):
    """Функция сложения."""
    return a + b


def sub(a, b):
    """Функция вычитания."""
    return a - b


def mul(a, b):
    """Функция умножения."""
    return a * b


def div(a, b):
    """Функция деления."""
    if b == 0:
        raise ValueError("Деление на ноль")
    print('OK 123')
    return a / b


def get_num():
    return random.randint(1, 100)