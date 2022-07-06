import sys

from functools import partial, wraps, lru_cache


def demo_partial():
    print(pow(2, 3))
    print(pow(3, 4))

    # never assign lambda!!
    pow2 = lambda x: pow(x, 2)

    print(pow2(4))
    print(pow2(5))

    # never assign lambda!!
    pow_num3 = lambda x: pow(3, x)
    print(pow_num3(2))
    print(pow_num3(3))

    print(list(map(pow_num3, [3, 4, 5])))

    pow3 = partial(pow, exp=3)
    print(pow3(2))
    print(pow3(3))

    pow_num4 = partial(pow, 4)

    print(pow_num4(2))
    print(pow_num4(3))

    print(list(map(pow_num4, [4, 5, 6])))


def trace_fib(func):

    fib_cache = {}

    func._count = 0
    func._cache = fib_cache

    @wraps(func)
    def wrapper(n: int):
        print("--" * func._count + f"--> fib({n})")
        if n in fib_cache:
            result = fib_cache[n]
        else:
            func._count += 1
            result = func(n)
            func._count -= 1
            fib_cache[n] = result

        print("*--" + "--" * func._count, f"fib({n}) = {result}")
        return result

    return wrapper


# @lru_cache
@trace_fib
def fib(n: int):
    """
    fib:
    0 1 1 2 3 5 8 13
    :param n:
    :return:
    """
    if n < 2:
        return n

    return fib(n - 1) + fib(n - 2)


def demo_fib():
    print(list(map(fib, range(100))))
    print(fib)
    print(fib.__wrapped__)
    print(fib.__wrapped__._cache)
    print(sys.getsizeof(fib.__wrapped__._cache))
    print(sys.getsizeof({}))


def main():
    # demo_partial()
    demo_fib()


if __name__ == '__main__':
    main()
