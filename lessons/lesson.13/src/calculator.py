def add(number_a: int, number_b: int) -> int:
    """ Складываем два числа. """
    return number_a + number_b


def subtract(number_a: int, number_b: int) -> int:
    """ Вычитаем второе число из первого. """
    return number_a - number_b


def multiply(number_a: int, number_b: int) -> int:
    """ Умножаем два числа. """
    return number_a * number_b


def divide(number_a: int, number_b: int) -> float:
    """ Делим первое число на второе. """
    if number_b == 0:
        raise ZeroDivisionError("Деление на ноль запрещено")
    return number_a / number_b


# if __name__ == '__main__':
#     print(add(2, 3))
#     print(subtract(2, 3))
#     print(multiply(2, 3))
#     print(divide(2, 3))
