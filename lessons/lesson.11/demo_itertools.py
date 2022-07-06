from collections import Counter
from itertools import (
    cycle,
    chain,
    count,
)


# def my_cycle(iterable):
#     while True:
#         for i in iterable:
#             yield i


def demo_cycle():
    n = cycle([2, 3])
    print(
        list(
            map(pow, n, range(10))
        )
    )
    print(list(range(10)))

    print(
        list(
            map(pow, n, [3, 2, 5])
        )
    )

    print(next(n))
    print(next(n))
    print(next(n))
    print(next(n))
    print(next(n))


def demo_chain():
    names = ["Kate", "Jim", "Nick"]
    surnames = ["White", "Black", "Smith"]
    emails = ["a@b.com", "john@examle.com"]
    age_ranges = [["0-10"], ["11-20"], ["21-30"]]

    result = chain(names, surnames, emails, *age_ranges)
    print(list(result))


def demo_counter():
    items = [1, 1, 1, 1, 2, 2, 2, 2, 1, 4, 3, 3, 3, 3, 3, 3, 5, 3, 5]
    items_count = Counter(items)
    print(items_count)
    print("3 count:", items_count[3])
    print(help(Counter))


def demo_count():
    cnt = count(0)
    # print(cnt)
    # for i in cnt:
    #     print(i)

    n = cycle([2])
    print(list(map(
        lambda x, y, *a: x ** y,
        n,
        range(3, 24, 3),
        cnt,
    )))
    print(cnt)
    # help(count)

    c = count(1, step=3)
    print(list(zip(range(15, 40, 4), c)))


def main():
    # demo_cycle()
    # demo_chain()
    # demo_counter()
    demo_count()


if __name__ == '__main__':
    main()
