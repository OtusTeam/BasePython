def squares(*nums: int) -> list[int]:
    return [n * n for n in nums]


def main():
    sqs = squares(1, 2, 3, 4)
    print(squares(1, 2, 3))
    print(sqs)
    print(1, 2, 3, 4)
    print(*sqs)

    first = sqs[0]
    print("first:", first)
    first, second, *_ = sqs
    print("first:", first, "second:", second)

    a = 3
    b = 7
    print(a, b)
    a, b = b, a
    print(a, b)


if __name__ == "__main__":
    main()
