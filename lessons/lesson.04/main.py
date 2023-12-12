def demo_map():
    odds = [i for i in range(10) if i % 2]
    exps = [i for i in range(6, 1, -1)]
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


def demo_zip():
    evens = [
        i
        for i in range(1, 20)
        if i % 2 == 0
    ]
    nums = list(range(10, 30, 3))
    print(evens)
    print(nums)

    for e, n in zip(evens, nums):
        print(e, n, n - e)


def main():
    print("Hello World!")
    demo_map()
    demo_zip()


if __name__ == "__main__":
    main()
