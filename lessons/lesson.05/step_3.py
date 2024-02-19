def fib(n):
    """
    fib(0) = 0
    fib(1) = 1
    fib(n) = fib(n - 1) + fib(n - 2)
    """
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b

    return a


def fib_g():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


def main():
    print([fib(i) for i in range(11)])
    f = fib_g()
    print(next(f))
    print(next(f))

    f = fib_g()
    print([next(f) for _ in range(11)])
    print(next(f))
    for _ in range(5):
        print(next(f))

    for n in fib_g():
        if n > 100:
            print("found fibonacci number", n)
            break

    # for n in fib_g():
    #     print(n % 10**10)


if __name__ == "__main__":
    main()
