from functools import cache


@cache
def factorial(n):
    # if n > 0:
    #     raise ValueError("...")

    print("find f for", n)
    if n < 3:
        return n

    return factorial(n - 1) * n


@cache
def fibonacci(n):
    if n < 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


@cache
def get_currency_rates(from_currency, to_currency, datetime):
    print("currency for", from_currency, to_currency, datetime)
    return 42


def main():
    get_currency_rates("A", "B", "...")
    print(get_currency_rates.cache_info())
    get_currency_rates("A", "B", "...")
    get_currency_rates("A", "B", "...")
    print(get_currency_rates.cache_info())
    get_currency_rates.cache_clear()
    print(get_currency_rates.cache_info())
    get_currency_rates("A", "B", "...")
    print("now kw")
    get_currency_rates("A", "B", datetime="...")
    get_currency_rates("A", "B", datetime="...")
    print("now kw2")
    get_currency_rates("A", to_currency="B", datetime="...")

    print()
    print()
    print(factorial(5))
    print(factorial(10))
    print(factorial(10))
    print(factorial(10))
    for i in range(10):
        print(i, factorial(i))

    print([
        fibonacci(n)
        for n in range(1, 41)
    ])


if __name__ == '__main__':
    main()
