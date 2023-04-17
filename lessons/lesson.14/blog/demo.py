def caller(func, *args):
    print("call func", func, "with args", args)
    return func(*args)


def power(num, exp):
    return num ** exp


def is_even(num):
    return num % 2 == 0


def main():
    result = caller(sum, [1, 2, 3, 4])
    print(result)
    result = caller(power, 2, 3)
    print(result)
    result = caller(lambda x: x * x, 4)
    print(result)
    # nums = list(range(1, 13, 2))
    nums = [23, 43, 23, 13, 3, 53, 75, 58, 68, 9, 78]
    print(nums)
    result = list(
        filter(
            lambda num: num % 2 == 0,
            # is_even,
            nums
        )
    )
    print(result)


if __name__ == "__main__":
    main()
