from itertools import count
from collections import Counter


def demo_enumerate():
    # i = 0
    for i, num in enumerate(range(10, 20, 3), start=1):
        print(i, num)

    # print(i)


def demo_count_zip():
    c = count()

    for num, _ in zip(range(1002), c):
        if num ** num > 1000:
            break

    print(c)


def demo_count():
    c = count(1)

    for num in map(pow, range(30, 100, 7), c):
        print(num)

    print(c)


def demo_counter():
    line = "hello world!"
    count_letters = Counter(line)
    print(count_letters)

    names = ["John", "Bob", "Alice", "Kate", "Bob", "Alice", "Bob"]
    count_names = Counter(names)
    print(count_names)
    print(count_names.most_common(3))


def main():
    # demo_count()
    # demo_enumerate()
    demo_counter()


if __name__ == '__main__':
    main()
