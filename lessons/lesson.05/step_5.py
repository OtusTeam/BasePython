def is_even(n):
    return n % 2 == 0
    # return not n % 2


def main():
    numbers = [
        1,
        3,
        7,
        11,
        12,
        15,
        19,
        21,
        23,
        24,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
    ]
    evens = [n for n in numbers if n % 2 == 0]
    print(evens)
    evens = [n for n in numbers if is_even(n)]
    print(evens)

    for n in numbers:
        if not is_even(n):
            continue
        print("The number", n, "is even")

    for n in (n for n in numbers if is_even(n)):
        print("The number", n, "is even")

    for n in filter(is_even, numbers):
        print("The number", n, "is even")

    print(filter(is_even, numbers))
    print(list(filter(is_even, numbers)))


if __name__ == "__main__":
    main()
