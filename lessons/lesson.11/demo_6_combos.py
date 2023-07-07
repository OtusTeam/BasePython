from pprint import pprint

from itertools import (
    combinations,
    combinations_with_replacement,
    permutations,
    product,
)

names_male = ["Pete", "John", "Nick"]
names_female = ["Kate", "Alice"]
names = names_male + names_female


def demo_combinations():
    pairs = combinations(names, 2)
    pprint(list(pairs))
    trio = combinations(names, 3)
    pprint(list(trio))


def demo_combinations_with_replacement():
    combos = combinations_with_replacement(names, 3)
    pprint(list(combos))


def demo_permutations():
    todos = ["wash", "eat", "dress"]
    result = permutations(todos, 3)
    pprint(list(result))


def demo_product():
    pairs = product(names_male, names_female)
    pprint(list(pairs))


def main():
    demo_combinations()
    print()
    demo_combinations_with_replacement()
    print()
    demo_permutations()
    print()
    demo_product()


if __name__ == '__main__':
    main()
