def contains_duplicates(elements):
    known_elements = set()
    # print("Inited known elements:", known_elements)
    for element in elements:
        if element in known_elements:
            return True
        known_elements.add(element)
        # print(known_elements)
    return False


words = [
    "apple",
    "eggs",
    "banana",
    "eggs",
    "house",
    "bicycle",
    "spam",
]

numbers = [1, 2, 3, 2, 5, 6]

print(contains_duplicates(words))
print(contains_duplicates(numbers))
numbers[3] = 4
print(contains_duplicates(numbers))


def main():
    elements = (1, 2, 3, 4, 5, 6)
    print(contains_duplicates(elements))


main()

print(contains_duplicates("1231"))
# print(contains_duplicates(True))
