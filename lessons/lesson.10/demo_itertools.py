import string
from pprint import pprint
from itertools import (
    combinations,
    combinations_with_replacement,
    permutations,
    zip_longest,
    cycle,
    chain,
)

nums = list(range(10))


def demo_combinations():
    pprint(list(combinations(nums, 2)))
    pprint(list(combinations(nums, 3)))
    pprint(list(combinations(nums, 4)))


def demo_combinations_with_replacement():
    pprint(list(combinations_with_replacement(nums, 2)))
    pprint(list(combinations_with_replacement(nums, 3)))
    pprint(list(combinations_with_replacement(nums, 4)))


def demo_permutations():
    pprint(list(permutations(nums, 2)))
    pprint(list(permutations(nums, 3)))
    pprint(list(permutations(nums, 4)))


def demo_zip_longest():
    nums5 = list(range(5))
    pprint(list(zip(nums, nums5)))

    pprint(list(zip_longest(nums, nums5, fillvalue=-1)))


def demo_cycle():
    default_ids = list("ABC")

    pprint(list(zip(nums, cycle(default_ids))))


def demo_chain():
    letters = list(string.ascii_letters)
    print("letters:", letters)
    punctuation = list(string.punctuation)
    print("punctuation:", punctuation)
    digits = list(range(30))
    print("digits:", digits)

    all_we_have = chain(letters, digits, punctuation)
    pprint(list(all_we_have))

    first_names = [
        ["Sam", "Ann"],
        ["Nick", "Jack", "John"],
        ["James"],
    ]
    last_names = [
        ["White", "Black", "Brown"],
        ["Smith", "Potter"],
    ]
    all_names = list(chain(*first_names, *last_names))
    pprint(all_names)

    f_names = list(chain.from_iterable(first_names))
    l_names = list(chain.from_iterable(last_names))
    pprint(f_names)
    pprint(l_names)


def main():
    demo_combinations()
    demo_combinations_with_replacement()
    demo_permutations()
    demo_zip_longest()
    demo_cycle()
    demo_chain()


if __name__ == '__main__':
    main()

