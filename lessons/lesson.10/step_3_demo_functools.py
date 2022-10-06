from functools import wraps, lru_cache, partial


def trace_with_one_arg(func):

    func._count = 0

    @wraps(func)
    def wrapper(n):
        print("--" * func._count, f"--> {func.__name__}({n})")
        func._count += 1
        result = func(n)
        func._count -= 1
        print("*---" + "--" * func._count, f"{func.__name__}({n}) = {result!r}")

        return result

    return wrapper


@lru_cache
@trace_with_one_arg
def fib(n: int):
    """
    fib
    0 1 1 2 3 5 8 13
    :param n:
    :return:
    """
    if n < 2:
        return n

    return fib(n - 1) + fib(n - 2)


def demo_partial():
    print(pow(2, 2))
    print(pow(3, 2))
    print(pow(4, 2))

    # never assign lambda!
    pow2 = lambda x: pow(x, 2)
    print(pow2(2))
    print(pow2(3))
    print(pow2(4))

    # never assign lambda!
    pow_num3 = lambda x: pow(3, x)
    print(pow_num3(2))
    print(pow_num3(3))
    print(pow_num3(4))

    pow3 = partial(pow, exp=3)
    print(pow3(2))
    print(pow3(3))
    print(pow3(4))

    pow_num4 = partial(pow, 4)
    print(pow_num4(2))
    print(pow_num4(3))
    print(pow_num4(4))

    print(list(map(pow3, range(4))))

    class MyClass:
        def __init__(self, param1, param2):
            self.param3 = param1 + param2

    print(partial(int, base=2)("1010"))

    p = partial(MyClass, param2="qwerty")
    r = p("abc")
    print(r.param3)


if __name__ == '__main__':
    # print(list(map(fib, range(10))))
    # print(list(map(fib, range(100))))
    demo_partial()
