from typing import Callable
import random


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


@dec_number
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



if __name__ == '__main__':
    func_game(170, -3)
