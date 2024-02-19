def square(n):
    return n * n


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
    squares = [square(n) for n in numbers]
    print(squares)

    for sq in map(square, numbers):
        print("sq:", sq)

    print(map(square, numbers))
    print(list(map(square, numbers)))


if __name__ == "__main__":
    main()
