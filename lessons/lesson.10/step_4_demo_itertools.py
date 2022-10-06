from pprint import pprint
from itertools import repeat, chain, combinations, permutations, combinations_with_replacement


def demo_repeat():

    r_spam = repeat("spam")
    for a, b in zip(range(5), r_spam):
        print(a, b)

    print(list(map(pow, range(10), repeat(2))))


def demo_chain():
    names_female = ["Kate", "Alice"]
    names_male = ["Peter", "Bob", "Jack"]

    all_names = [*names_female, *names_male]

    names = [names_female, names_male]
    # print(all_names)
    print(names)
    print(list(chain(*names)))
    print(list(chain.from_iterable(names)))
    print(list(chain(names_female, names_male)))


def demo_combinations():
    nums = list(range(1, 11))
    pprint(list(combinations(nums, 2)))
    pprint(list(combinations(nums, 3)))
    pprint(list(combinations(nums, 7)))


if __name__ == '__main__':
    # demo_repeat()
    # demo_chain()
    demo_combinations()
