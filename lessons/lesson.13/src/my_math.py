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
    return a / b


def gen_rand(start, stop):
    num =  random.randint(start, stop)
    return f'Число {num}'