from pprint import pprint
from itertools import cycle, repeat


def demo_cycle():
    names = cycle([
        "John",
        "Sam",
        "Bob",
    ])
    for _ in range(10):
        print(next(names))

    ideas = [
        "Idea 1",
        "Idea 2",
        "Idea 3",
        "Idea 4",
        "Idea 5",
    ]
    for idea, name in zip(ideas, names):
        print(idea, name)
    # print(next(names))
    # print(next(names))
    # print(next(names))


def demo_repeat():
    # num_2 = cycle([2])
    # num_2 = repeat(2, times=3)
    # num_2 = repeat(2)
    power = repeat(3)

    pprint(list(map(pow, range(1, 10), power)))


def main():
    demo_repeat()


if __name__ == '__main__':
    main()
