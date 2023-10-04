from functools import cache
# from functools import wraps
# from functools import partial



@cache
def fib(n):
    print("find fib for", n)
    if n < 2:
        return n

    return fib(n - 1) + fib(n - 2)


def main():
    print(fib(10))
    print(fib(5))
    print(fib(6))
    print(fib(9))
    print(fib(n=11))
    print(fib(11))
    print(fib(100))
    print(fib(10))
    print(fib(20))


if __name__ == "__main__":
    main()
