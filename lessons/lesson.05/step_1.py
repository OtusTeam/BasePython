def main():
    numbers = [1, 3, 7, 11, 12, 15, 19, 21, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]
    print(iter(numbers))
    print(next(iter(numbers)))
    print("tuple of squares", tuple(n * n for n in numbers))
    for num in (n * n for n in numbers):
        print("square is", num)

    # for num in iter(numbers):
    for num in numbers:
        s = num * num
        print("1. square is", s)
        if s > 400:
            break

    for num in numbers:
        s = num * num
        print("2. square is", s)

    squares_g = (n * n for n in numbers)
    print("squares_g is", squares_g)
    print(next(squares_g))
    print(next(squares_g))
    print(next(squares_g))
    for s in squares_g:
        print("1. s:", s)
        if s > 600:
            break

    print(next(squares_g))
    for s in squares_g:
        print("2. s:", s)


if __name__ == "__main__":
    main()
