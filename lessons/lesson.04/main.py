from itertools import zip_longest


def create_file_with_lines():
    lines = [
        f"line {i:03d}\n"
        for i in range(1, 51)
    ]

    with open("text.txt", "w") as f:
        f.writelines(lines)


def demo_walrus_operator():
    a = ["spam"]
    # items_count = len(a)
    if items_count := len(a):
        print("items count", items_count)
    else:
        print("no items")


def demo_map():
    print(pow(2, 3))
    for i in map(pow, [2, 3, 4], [5, 3, 2]):
        print("i =", i)


def demo_zip():
    # print(list(zip(range(10), range(10, 20), range(50, 30, -2))))
    # for item in zip(range(15), range(10, 20), range(50, 30, -2)):
    #     print(item)
    for a, b, c in zip(range(15), range(10, 20), range(50, 30, -2)):
        print(a, b, c)

    list_of_strings = ["spam", "eggs", "foo", "bar", "num"]
    some_data = {
        "a": "A",
        "spam": "eggs",
        "foo": "bar",
        "fizz": "buzz",
        "data": {"spam": "eggs", 1: 111},
    }
    for item, (key, value) in zip(list_of_strings, some_data.items()):
        print(item, key, value)


def demo_zip_longest():
    for a, b in zip_longest(range(10), range(4), fillvalue=-1):
        print(a, b)


def main():
    print("starting")
    create_file_with_lines()
    demo_walrus_operator()
    demo_map()
    demo_zip()
    demo_zip_longest()
    print("done..")


if __name__ == '__main__':
    main()
