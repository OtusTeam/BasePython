def fruits_upper_gen(items):
    for el in items:
        yield el.upper()


fruits = ['apple', 'peach', 'lemon']
fruits_upper_2 = map(str.upper, fruits)

print(*fruits_upper_2)

fruits_3 = fruits_upper_gen(fruits)
# fruits_3_as_list = list(fruits_upper_gen(fruits))
print(type(fruits_3))
print(next(fruits_3))
print(next(fruits_3))
print(next(fruits_3))
# print(next(fruits_3))
# print(*fruits_upper_gen(fruits))
