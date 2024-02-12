fruits = ["apple", "banana", "cherry"]
vegetables = ["potato", "cucumber"]


def print_items(elements):
    if elements:
        print("first element: ", elements[0])
    else:
        print("no elements")

    for item in elements:
        print("•", item)


print("Hello")
print("fruits:")
print_items(fruits)
print("vegetables:")
print_items(vegetables)
print_items([])
