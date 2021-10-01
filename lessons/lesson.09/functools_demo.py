from typing import Sequence
from functools import wraps, lru_cache, partial

import tkinter


def trace(func):
    # func.level = 0
    @wraps(func)
    def inner(*args, **kwargs):
        print(func.__doc__)
        # args_str = ", ".join(map(repr, args))
        # kwargs_str = ", ".join(map(lambda k, v: f"{k}={v!r}", kwargs.items()))
        # func_args = list(filter(bool, (args_str, kwargs_str)))
        # print("__" * func.level + f"-> {func.__name__}({', '.join(func_args)})")
        # func.level += 1
        print(f'{func.__name__} start with args: {args} and kwargs: {kwargs}')
        result = func(*args, **kwargs)
        print(f'{func.__name__} end with res: {result}')

        # func.level -= 1
        # print("__" * func.level + f"<- {func.__name__}({', '.join(func_args)}) == {res}")

        return result
    return inner


@trace
def print_odd_numbers():
    '''Docstring'''
    for i in range(1, 15, 2):
        print(i)


# print_odd_numbers()


# cache = {}
# if args in cache:
#     return cache[args]
# res = func(*args)
# cache[args] = res

@lru_cache(maxsize=2048)
@trace
def fib(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)


# fib(8) -> fib(7) + fib(6)
# fib(7) -> fib(6) + fib(5)
# fib(6) -> fib(5) + fib(4)
# print(fib.__name__)
# print(fib.__module__)
# # print(fib(8))
# print(fib(42))


def get_data(data: dict, names: Sequence[str]):
    return [data.get(name) for name in names]


# def press_button(username):
#     print(f"{username} pressed a button ! ")
#
#
# root = tkinter.Tk()
# root.geometry('400x400')
# # button = tkinter.Button(text="press me!", command=press_button('Nigar')).pack()
# button = tkinter.Button(text="press me!", command=partial(press_button, 'Nigar')).pack()
# root.mainloop()


# names = ["position", "name"]
#
# get_position = partial(get_data, names=names)
#
# print(get_position({"name": "John", "position": "Engineer"}))
# print(get_position({"position": "Manager"}))


