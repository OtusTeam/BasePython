from functools import cache


@cache
def factorial(n):
    print("get factorial for n", n)
    if n < 2:
        return n
    return n * factorial(n - 1)


def main():
    print(factorial(3))
    print(factorial(4))
    print(factorial(5))
    print(factorial(6))


if __name__ == "__main__":
    main()
