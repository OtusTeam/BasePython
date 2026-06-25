from typing import Callable
import random
import json
from pathlib import Path
from functools import wraps


def my_logger(func):
    file = Path(f'{func.__name__}.json')
    if file.is_file():
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = []

    def wrapper(*args, **kwargs):
        new_dict = {'args': args, **kwargs}
        result = func(*args, **kwargs)
        new_dict['result'] = result

        data.append(new_dict)

        with open(file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    return wrapper


def dec_number(func):
    LOW_NUM = 1
    UP_NUM = 100
    LOW_COUNT = 1
    UP_COUNT = 10

    def wrapper(num: int, count: int, *args, **kwargs):
        if num < LOW_NUM or num > UP_NUM:
            print(f'Вышли из диапазона. {num=}')
            num = random.randint(LOW_NUM, UP_NUM)
            print(f'Новое значение {num=}')

        if count < LOW_COUNT or count > UP_COUNT:
            print(f'Вышли из диапазона. {count=}')
            count = random.randint(LOW_COUNT, UP_COUNT)
            print(f'Новое значение {count=}')

        result = func(num, count, *args, **kwargs)
        return result

    return wrapper


def count_func(number: int = 1):
    def deco(func):
        counter = []
        def wrapper(*args, **kwargs):
            for _ in range(number):
                result = func(*args, **kwargs)
                counter.append(result)
            return counter
        return wrapper
    return deco


# @my_logger
# @dec_number
@count_func(3)
def func_game(num: int, count: int):
    for i in range(1, count + 1):
        print(f'Попытка № {i}')
        answer = int(input('Введите число: '))
        if answer == num:
            print("Угадал")
            break
        elif answer > num:
            print("Твоё число больше")
        elif answer < num:
            print("Твоё число меньше")
    else:
        print(f'Попытки закончились. Загаднное число {num}')


@count_func(3)
# @my_logger
def get_num(num, *args, **kwargs):
    return num * 10

if __name__ == '__main__':
    func_game(120, 2)
    get_num(17, 1, 3, 6, 'a', qwerty=123, qaz=146)
