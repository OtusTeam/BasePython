def demo_map():
    nums = [i for i in range(10) if i % 2]
    exps = [i for i in range(6, 1, -1)]
    print(nums)
    print(exps)
    result = list(
        map(
            pow,
            nums,
            exps,
        )
    )
    print(result)


def demo_zip():
    evens = [i for i in range(1, 20) if i % 2 == 0]
    nums = list(range(10, 30, 3))
    print(evens)
    print(nums)

    for i, n in zip(evens, nums):
        print(i, n, i ** n)


def main():
    demo_zip()
    demo_map()


if __name__ == "__main__":
    main()
