from functools import wraps, lru_cache, partial


def trace(func):
    func.level = 0

    @wraps(func)
    def inner(*args, **kwargs):
        print("___" * func.level, f" --> {func.__name__}({args[0]})")
        func.level += 1
        res = func(*args, **kwargs)
        func.level -= 1
        print("___" * func.level, f" <-- {func.__name__}({args[0]}) == {res}")
        return res

    return inner


def my_cache(func):
    cache = {}

    @wraps(func)
    def inner(*args):
        if args in cache:
            return cache[args]

        res = func(*args)
        cache[args] = res
        return res

    return inner


@lru_cache(maxsize=2048)
# @my_cache
@trace
def fib(n):
    """Calc fib"""
    if n < 0:
        return None
    if n < 2:
        return 1

    return fib(n - 1) + fib(n - 2)


def partials():
    pow2 = lambda x: pow(x, 2)
    pow3 = partial(pow, exp=3)
    print("pow2 2", pow2(2))
    print("pow2 3", pow2(3))
    print("pow2 4", pow2(4))
    print("pow2 5", pow2(5))
    print("pow3 2", pow3(2))
    print("pow3 3", pow3(3))
    print("pow3 4", pow3(4))
    print("pow3 5", pow3(5))


def main():
    # print("call fib", fib, fib.__doc__)
    # print(fib(20))
    partials()


if __name__ == '__main__':
    main()
