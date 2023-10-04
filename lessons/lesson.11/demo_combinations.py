from itertools import combinations
from itertools import combinations_with_replacement
from itertools import permutations
from itertools import product
from itertools import count
# from itertools import repeat
# from itertools import cycle


names_male = ["Pete", "John", "Nick"]
names_female = ["Kate", "Alice", "Jan"]
names = names_male + names_female


def demo_combinations():
    pairs = combinations(names, 2)
    for pair in pairs:
        print(pair)


def demo_combinations_with_replacement():
    pairs = combinations_with_replacement([
        "apple", "banana", "orange", "mango"], 2)
    for pair in pairs:
        print(pair)


def demo_permutations():
    todos = ["wash", "eat", "dress"]
    result = permutations(todos, 3)
    for res in result:
        print(res)


def demo_product():
    pairs = product(names_male, names_female)
    for pair in pairs:
        print(pair)


def demo_count():
    c = count(1)
    for cnt, value in zip(c, range(10, 20, 2)):
        print(cnt, value)

    for cnt, value in zip(c, range(15, 30, 3)):
        print(cnt, value)


if __name__ == "__main__":
    # demo_combinations()
    # demo_combinations_with_replacement()
    # demo_permutations()
    # demo_product()
    demo_count()
