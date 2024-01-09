from itertools import combinations
from itertools import combinations_with_replacement
from itertools import permutations
from itertools import product
# from itertools import count

names_male = ["Pete", "John", "Nick"]
names_female = ["Kate", "Alice", "Jan"]
names = names_male + names_female

foods = ["apple", "banana", "orange", "kiwi"]


def demo_combinations():
    pairs = combinations(names, 2)
    for pair in pairs:
        print(pair)


def demo_combinations_with_replacement():
    pairs = combinations_with_replacement(foods, 2)
    for pair in pairs:
        print(pair)


def demo_permutations():
    actions = ["eat", "dress", "wash"]
    for result in permutations(actions, 3):
        print(result)


def demo_product():
    pairs = product(names_male, names_female)
    for pair in pairs:
        print(pair)


def main():
    # demo_combinations()
    # demo_combinations_with_replacement()
    # demo_permutations()
    demo_product()


if __name__ == "__main__":
    main()
