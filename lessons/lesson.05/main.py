def demo_zip():
    evens = [
        num for num in range(2, 20, 2)
    ]
    nums = list(range(10, 30, 3))
    print(len(evens), evens)
    print(len(nums), nums)

    for e, n in zip(evens, nums):
        print(e, n, n - e)


def demo_map():
    odds = [
        num for num in range(10)
        if num % 2
    ]
    exps = list(range(6, 1, -1))
    print(odds)
    print(exps)

    result = list(
        map(
            pow,
            odds,
            exps,
        )
    )
    print(result)


def main():
    print("Hello World!")
    demo_zip()
    demo_map()


if __name__ == "__main__":
    main()
