def to_upper(items):
    fruits_upper = []
    for el in items:
        fruits_upper.append(el.title())

    return fruits_upper  # + 10 ** 9


# .sort(), sorted()
fruits = ['apple', 'peach', 'lemon']  # 10 ** 9
# fruits = ['Apple', 'Peach', 'Lemon']

print(fruits)
result = to_upper(fruits)
# print(result[2])
# print(next(result))  # -> 'Apple', O(1)
# print(next(result))  # -> 'Peach'
# print(next(result))  # -> 'Lemon'
for el in result:
    print(el)
