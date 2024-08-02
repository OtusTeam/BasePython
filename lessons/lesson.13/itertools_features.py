import itertools
from termcolor import colored
from functools import partial
import time
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

# Пример использования count для генерации последовательных идентификаторов
id_generator = itertools.count(start=1, step=1)
print_green("Generated IDs:")
for _ in range(5):
    print_yellow(next(id_generator))

# Пример использования cycle для циклического выполнения задач
tasks = itertools.cycle(['task1', 'task2', 'task3'])
print_green("Cyclic tasks:")
for _ in range(6):
    print_yellow(next(tasks))

# Пример использования repeat для создания повторяющихся значений
print_green("Repeated messages:")
repeater = itertools.repeat('Repeat this message', 3)
for item in repeater:
    print_red(item)

# Пример использования combinations для генерации тестовых случаев
fields = ['username', 'password', 'email']
required_fields = itertools.combinations(fields, 2)
print_green("Test cases with required fields:")
for combination in required_fields:
    print_yellow(combination)

# Пример использования dropwhile и takewhile для фильтрации данных
data = [1, 2, 3, 4, 5, 6]
dropped_data = itertools.dropwhile(lambda x: x < 4, data)
print_green("Data after dropwhile (x < 4):")
for item in dropped_data:
    print_yellow(item)

taken_data = itertools.takewhile(lambda x: x < 4, data)
print_green("Data after takewhile (x < 4):")
for item in taken_data:
    print_red(item)

# Пример использования chain для объединения нескольких итераторов
iter1 = [1, 2, 3]
iter2 = ['A', 'B', 'C']
combined = itertools.chain(iter1, iter2)
print_green("Combined iterators:")
for item in combined:
    print_yellow(item)
