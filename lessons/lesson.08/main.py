from typing import TypeVar

TAddParam = TypeVar("TAddParam", int, float, str)


def add(a: TAddParam, b: TAddParam) -> TAddParam:
    return a + b


def main():
    print(add(1, 2))
    # print(add("1", 1))
    # print(add(1, "1"))
    res = add(1, 2)
    # print(res + "1")
    res = add("1", "2")
    # print(res + 1)
    # print(add(2, 1.0))
    print(add(1, "1"))


if __name__ == "__main__":
    main()
