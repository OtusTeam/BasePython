import time
from functools import partial, wraps, lru_cache, reduce, total_ordering
from termcolor import colored
import os

os.system("clear")

"""
для работы необходима установка библиотеки termcolor

pip3 install -r requirements.txt
"""

# Стартовое время для измерения текущего времени
start_time = time.time()


def current_time():
    return round(time.time() - start_time, 2)


def print_color(message, color):
    print(colored(f"[{current_time()}s] {message}", color))


# Использование partial для создания новых функций с фиксированными аргументами
print_green = partial(print_color, color="green")
print_yellow = partial(print_color, color="yellow")
print_red = partial(print_color, color="red")

# Примеры использования созданных функций
# print_green("Зеленое сообщение.")
# print_yellow("Желтое сообщение.")
# print_red("Красное сообщение.")


# Пример использования wraps для создания декоратора
def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print_yellow(f"Функция {func.__name__} выполнилась за {end - start:.3f} секунд")
        return result

    return wrapper


@timing_decorator
def slow_function():
    '''this function is slow'''
    print_green('start')
    time.sleep(1)
    return "Готово!"

# slow_function()
# help(slow_function)


# Пример использования reduce для суммирования
numbers = [1, 2, 3, 4, 5]
# sum_result = reduce(lambda x, y: x + y, numbers)
# print_green(f"Sum of {numbers}: {sum_result}")
# # Пример вызова декорированной функции
# print_green(slow_function())


# Пример использования lru_cache для мемоизации
@timing_decorator
@lru_cache(maxsize=3)
def func_hard(limit):
    squares = [i**i for i in range(limit)]
    return reduce(lambda a, b: a + b, squares)


# print_green('limit = 10000')
# func_hard(10000)
# func_hard(10000)
# func_hard(10000)
# print_green('limit = 11000')
# func_hard(11000)
# print_green('limit = 9000')
# func_hard(9000)
# print_green('limit = 11000')
# func_hard(11000)
# print_green('limit = 10000')
# func_hard(10000)
# func_hard(10000)
# func_hard(10000)


# Пример использования total_ordering для упрощения сравнения объектов
@total_ordering
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age


# Создаем экземпляры класса
alice = Person("Alice", 30)
bob = Person("Bob", 30)

# # Проверяем операции сравнения
# print_green(f"Alice > Bob: {alice > bob}")
# print_green(f"Alice <= Bob: {alice <= bob}")
# print_green(f"Alice == Bob: {alice == bob}")
# print_green(f"Alice != Bob: {alice != bob}")
