from typing import Sequence
from functools import wraps, lru_cache, partial


def trace(func):
    func.level = 0
    @wraps(func)
    def inner(*args, **kwargs):
        args_str = ", ".join(map(repr, args))
        kwargs_str = ", ".join(map(lambda k, v: f"{k}={v!r}", kwargs.items()))
        func_args = list(filter(bool, (args_str, kwargs_str)))
        print("__" * func.level + f"-> {func.__name__}({', '.join(func_args)})")
        func.level += 1
        res = func(*args, **kwargs)
        func.level -= 1
        print("__" * func.level + f"<- {func.__name__}({', '.join(func_args)}) == {res}")
        return res
    return inner


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


print(fib.__name__)
print(fib.__module__)

print(fib(42))


def get_data(data: dict, names: Sequence[str]):
    return [data.get(name) for name in names]


names = ["position"]
get_position = partial(get_data, names=names)

print(get_position({"name": "John", "position": "Engineer"}))
print(get_position({"position": "Manager"}))
