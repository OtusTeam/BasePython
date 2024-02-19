def square(n):
    return n * n


def squares(*numbers):
    return [
        num * num
        for num in numbers
    ]


def main():
    print(square(2))
    print(square(3))
    print(square(4))

    print(squares(1, 2, 3, 4))
    print(squares(5, 6, 7, 8))

    # for num in range(1, 1000):
    num = 0
    while square(num) < 1000:
        num += 1

    print("largest num is", num)
    print("square is", square(num))

    numbers = [1, 3, 7, 11, 12, 15, 19, 21, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]
    print(squares(*numbers))
    for num in squares(*numbers):
        print("square is", num)
        if num >= 1_000:
            break

    print("list of squares", [n * n for n in numbers])
    for num in [n * n for n in numbers]:
        print("square is", num)

    print("tuple of squares", tuple(n * n for n in numbers))
    for num in (n * n for n in numbers):
        print("square is", num)


if __name__ == "__main__":
    main()
