from typing import TypeVar, reveal_type

IntOrFloat = TypeVar("IntOrFloat", float, int)


def cube(num: IntOrFloat) -> IntOrFloat:
    return num**3


def main() -> None:
    c1 = cube(5)
    reveal_type(c1)
    print(c1)

    c2 = cube(2.5)
    reveal_type(c2)
    print(c2)


if __name__ == '__main__':
    main()
