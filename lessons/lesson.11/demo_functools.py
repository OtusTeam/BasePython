from functools import cache
from functools import partial
# from functools import wraps


def big_func(foo, bar, spam, eggs):
    return locals()


@cache
def fib(n):
    print("find fib for n", n)
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def main():
    # print(
    #     big_func(
    #         "foo val",
    #         "bar another value",
    #         "spamspamspam",
    #         "eggs!",
    #     )
    # )
    # print(
    #     big_func(
    #         "foo val",
    #         "bar another value",
    #         "spamspamspam",
    #         "eggs (2)",
    #     )
    # )
    # print(
    #     big_func(
    #         "foo val",
    #         "bar another value",
    #         "spamspamspam",
    #         "eggs (3)",
    #     )
    # )
    func = partial(big_func, "foo val", bar="bar another value", eggs="eggs!!")
    print(func)
    print(func(spam="spamspam"))
    print(func(spam="2spam"))
    print(func(spam="3spam"))
    print(pow(2, 3))
    pow3 = partial(pow, exp=3)
    print(pow3(2))
    print(pow3(3))
    print(pow3(4))
    # print(fib(10))
    # print(fib(5))
    # print(fib(5))
    # print(fib(9))
    # print([fib(i) for i in range(1, 11)])

    # print(fib(50))
    # print(fib(100))


if __name__ == "__main__":
    main()
