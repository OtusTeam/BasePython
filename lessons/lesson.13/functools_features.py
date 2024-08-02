import time
from functools import partial, wraps, lru_cache, reduce, total_ordering
from termcolor import colored
import os

os.system('clear')

'''
Для лучшего понимания скрывайте многострочными комментариями код по частям

для работы необходима установка библиотеки termcolor

pip install termcolor
'''

# Стартовое время для измерения текущего времени
start_time = time.time()

def current_time():
    return round(time.time() - start_time, 2)

def print_color(message, color):
    print(colored(f"[{current_time()}s] {message}", color))

# Использование partial для создания новых функций с фиксированными аргументами
print_green = partial(print_color, color='green')
print_yellow = partial(print_color, color='yellow')
print_red = partial(print_color, color='red')

# Примеры использования созданных функций
print_green("This is a green message.")
print_yellow("This is a yellow message.")
print_red("This is a red message.")

# Пример использования wraps для создания декоратора
def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print_yellow(f"Executed {func.__name__} in {end - start:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(1)
    return "Done"

# Пример вызова декорированной функции
print_green(slow_function())

# Пример использования lru_cache для мемоизации
@lru_cache(maxsize=32)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print_green(f"fibonacci(10): {fibonacci(10)}")
print_green(f"fibonacci(15): {fibonacci(15)}")
print_green(f"fibonacci(20): {fibonacci(20)}")

# Пример использования reduce для суммирования
numbers = [1, 2, 3, 4, 5]
sum_result = reduce(lambda x, y: x + y, numbers)
print_green(f"Sum of {numbers}: {sum_result}")

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
bob = Person("Bob", 25)

# Проверяем операции сравнения
print_green(f"Alice > Bob: {alice > bob}")
print_green(f"Alice <= Bob: {alice <= bob}")
print_green(f"Alice == Bob: {alice == bob}") 
print_green(f"Alice != Bob: {alice != bob}")
