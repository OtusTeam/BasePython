"""
Main file
"""
from os import getenv


def demo_map():
    list_of_powers = list(
        map(
            pow,
            [1, 2, 3, 4, 5],
            [100, 10, 5, 0, 2],
        )
    )
    print(list_of_powers)


def demo_zip():
    values1 = list(range(2, 10))
    values2 = list(range(10, 29, 3))
    print(values1)
    print(values2)
    for v1, v2 in zip(values1, values2):
        print(f"{v1=}, {v2=}")
        print("sum =", v1 + v2)
        print("sub =", v1 - v2)


def main():
    print("hello world!", getenv("SECRET_KEY"))
    demo_map()
    demo_zip()


if __name__ == "__main__":
    main()
