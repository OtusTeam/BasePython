def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def divide(a, b):
    if b == 0:
        raise ValueError('divide by zero')
    return a / b