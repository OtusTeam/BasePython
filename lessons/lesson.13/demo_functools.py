# import sys
from functools import cache
from functools import partial
from functools import wraps


# from functools import lru_cache


# sys.setrecursionlimit(10000)


@cache
# @lru_cache(maxsize=100)
def factorial(n):
    if n < 2:
        return n
    return n * factorial(n - 1)


def demo_cache():
    print(factorial(5))
    print(factorial(50))
    print(factorial(500))
    print(factorial(50))
    print(factorial(500))
    print(factorial(50))
    print(factorial.cache_info())
    print(factorial(100))
    print(factorial.cache_info())
    print(factorial(n=100))
    print(factorial.cache_info())
    # print(factorial(1000))


def say_hi(name, greeting="Hi"):
    msg = f"{greeting}, {name}!"
    print(msg)
    return msg


def demo_partial():
    say_hi("Bob")
    say_hi("King", greeting="Hello")

    hello = partial(say_hi, greeting="Hello")
    hello("King")
    hello("Queen")
    hello(name="John")


def main():
    # demo_cache()
    demo_partial()


if __name__ == "__main__":
    main()
