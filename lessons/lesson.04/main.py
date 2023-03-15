def demo_map():
    list_of_powers = list(
        map(
            pow,
            range(1, 6),
            [100, 10, 5, 3, 0]
        )
    )
    print(list_of_powers)


def demo_zip():
    values_1 = list(range(2, 10))
    values_2 = list(range(10, 29, 3))
    print(values_1)
    print(values_2)

    for v1, v2 in zip(values_1, values_2):
        print(f"{v1=}, {v2=}")
        print("sum =", v1 + v2)
        print("sub =", v1 - v2)


def main():
    print("Hello world!")
    demo_map()
    demo_zip()


if __name__ == "__main__":
    main()
