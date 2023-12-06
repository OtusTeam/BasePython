fruits = ['apple', 'peach', 'lemon']
fruits_upper = []
for fruit in fruits:
    if fruit.startswith('a'):
        continue
    fruits_upper.append(fruit.upper())

print(fruits_upper)


def my_filter(fruit) -> bool:
    # return None
    # return
    return not fruit.startswith('a')


# fruits_upper_2 = filter(my_filter, fruits)
# print(*fruits_upper_2)
# fruits_upper_2 = list(filter(my_filter, fruits))
# fruits_upper_2 = list(map(str.upper, filter(my_filter, fruits)))
# fruits_upper_2 = list(map(str.upper, filter(lambda fruit: not fruit.startswith('a'), fruits)))
fruits_upper_2 = list(
    map(
        str.upper,
        filter(
            lambda x: not x.startswith('a'),
            fruits,
        ),
    ),
)
print(fruits_upper_2)

# str.upper('a')
# str.lower('A')
# dict.fromkeys(['hello'])

# new_fruits = fruits.append('bread')
