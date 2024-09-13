import itertools
import time
import os
from functools_features import print_yellow, print_green, print_red

os.system("clear")

"""
для работы необходима установка библиотеки termcolor

pip3 install -r requirements.txt
"""

# Пример использования count для генерации последовательных идентификаторов
# id_generator = itertools.count(start=1, step=1)
# print_green("Generated IDs:")
# for _ in range(5):
#     print_yellow(next(id_generator))

# Пример использования cycle для циклического выполнения задач


def print_hello():
    print_green("Hello")


def print_goodbye():
    print_red("Goodbye\n")


tasks = [print_hello, print_goodbye]

task_executor = itertools.cycle(tasks)

# for i in range(20):
#     task = next(task_executor)
#     task()
#     time.sleep(0.1)

# Пример использования repeat для создания повторяющихся значений
# print_green("Repeated messages:")
repeater = itertools.repeat("Будет повторяться")
# for item in repeater:
#     print_red(item)

# Пример использования combinations
fields = ["username", "password", "email"]
required_fields = itertools.combinations(fields, 2)
# print_green("Комбинации fields")
# for combination in required_fields:
#     print_yellow(combination)
#
# Пример использования dropwhile и takewhile для фильтрации данных
data = [1, 2, 3, 4, 5, 6, 3, 2, 1]
dropped_data = itertools.dropwhile(lambda x: x < 4, data)
# print_green("dropwhile (x < 4):")
# for item in dropped_data:
#     print_yellow(item)

taken_data = itertools.takewhile(lambda x: x < 4, data)
# print_green("takewhile (x < 4):")
# for item in taken_data:
#     print_red(item)

# Пример использования chain для объединения нескольких итераторов
iter1 = [1, 2, 3]
iter2 = ["A", "B", "C"]
combined = itertools.chain(iter1, iter2)
# print_green("Значения внутри объедененного итератора:")
# print_yellow(list(combined))

# Пример использования product для декартова произведения
colors = ['red', 'green']
sizes = ['S', 'M', 'L']
product_result = itertools.product(colors, sizes)
# print_green("Декартово произведение (product):")
# for item in product_result:
#     print_yellow(item)

# Пример использования permutations для всех возможных перестановок элементов
numbers = [1, 2, 3]
permutations_result = itertools.permutations(numbers, 3)
# print_green("Перестановки (permutations):")
# for item in permutations_result:
#     print_red(item)
