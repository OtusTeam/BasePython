from pprint import pprint
from itertools import (
    combinations,
    permutations,
    combinations_with_replacement,
    product,
)

names_male = ["Pete", "John", "Nick"]
names_female = ["Kate", "Alice"]
names = names_male + names_female


def demo_combinations():
    pairs = combinations(names, 2)
    pprint(list(pairs))
    trios = combinations(names, 3)
    pprint(list(trios))


def demo_permutations():
    result = permutations(names, 2)
    pprint(list(result))


def demo_combinations_with_replacement():
    result = combinations_with_replacement(names, 2)
    pprint(list(result))


def demo_product():
    # pairs = product(names_male, names_female)
    pairs = product(names_female, names_male)
    pprint(list(pairs))


def main():
    # demo_combinations()
    # demo_permutations()
    # demo_combinations_with_replacement()
    demo_product()


if __name__ == '__main__':
    main()
