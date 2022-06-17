def demo_map():
    list_of_powers = list(map(pow, [1, 2, 3, 4], [5, 4, 3, 2]))
    print(list_of_powers)


def demo_zip():
    values1 = list(range(2, 10))
    values2 = list(range(10, 29, 3))

    for v1, v2 in zip(values1, values2):
        print("v1 =", v1, "v2 =", v2, " sum =", v1 + v2)

    values3 = list(range(20, -7, -4))
    print("=" * 10)

    for v1, v2, v3 in zip(values1, values2, values3):
        print("v1 =", v1, "v2 =", v2, "v3 =", v3, " sum =", v1 + v2 + v3)


def main():
    # print("Hello main!")
    demo_map()
    demo_zip()


if __name__ == "__main__":
    main()
