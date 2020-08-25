from functools import wraps, partial, lru_cache
# from operator import pow

power_of_2 = lambda x: pow(x, 2)
print(power_of_2(2))
print(power_of_2(3))

p2 = partial(pow, exp=2)
print(p2(2))
print(p2(3))
print(p2(4))


p = partial(pow, 3)
# pow(3, ...)

print(p(1))
# pow(3, 1)

print(p(2))
# pow(3, 2)

print(p(3))
# pow(3, 3)


def trace(func):
    func.level = 0
    @wraps(func)
    def inner(*args, **kwargs):
        print('____' * func.level + ' --> {}({})'.format(func.__name__, args[0]))
        func.level += 1
        f = func(*args, **kwargs)
        func.level -= 1
        print('____' * func.level + ' <-- {}({}) == {}'.format(func.__name__, args[0], f))
        return f
    return inner


def my_lru_cache(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        try:
            return cache[args]
        except KeyError:
            pass
        res = func(*args)
        cache[args] = res
        return res

    return wrapper


# @lru_cache(maxsize=2048)
@my_lru_cache
@trace
def fib(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)


print([fib(n) for n in range(100)])
