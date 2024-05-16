from itertools import combinations
from itertools import combinations_with_replacement
from itertools import permutations
from itertools import product
from itertools import batched
from itertools import cycle
from itertools import count

names_male = ["Pete", "John", "Nick"]
names_female = ["Kate", "Alice", "Jan"]
names = names_male + names_female

foods = ["apple", "banana", "orange", "kiwi"]


def demo_combinations():
    print("combinations:")
    pairs = combinations(names, 2)
    for pair in pairs:
        print(pair)


def demo_combinations_with_replacement():
    print("combinations w/ replacement:")
    pairs = combinations_with_replacement(foods, 3)
    for pair in pairs:
        print(pair)


def demo_permutations():
    print("permutations:")
    actions = ["eat", "dress", "wash"]
    for result in permutations(actions, 3):
        print(result)


def demo_product():
    print("product:")
    pairs = product(names_male, names_female)
    for pair in pairs:
        print(pair)


def demo_batched():
    print("batched:")
    for batch in batched(foods, 3):
        print(batch)


def demo_cycle():
    print("cycle:")
    cycle_foods = cycle(foods)

    for name, food in zip(names, cycle_foods):
        print(name, "gets", food)


def demo_count():
    print("count:")
    c = count(1, 5)
    for name, idx in zip(names, c):
        print(idx, name)


def main():
    print()
    demo_combinations()
    print()
    demo_combinations_with_replacement()
    print()
    demo_permutations()
    print()
    demo_product()
    print()
    demo_batched()
    print()
    demo_cycle()
    print()
    demo_count()


if __name__ == "__main__":
    main()
