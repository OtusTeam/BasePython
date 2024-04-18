def to_upper(items):
    # fruits_upper = []
    for el in items:
        yield el.title()
    #     fruits_upper.append(el.title())
    #
    # return fruits_upper


# .sort(), sorted()
fruits = ['apple', 'peach', 'lemon']  # 10 ** 9
# fruits = ['Apple', 'Peach', 'Lemon']

print(fruits)
result = to_upper(fruits)
# print(result[2])
print(next(result))  # -> 'Apple', O(1)
print(next(result))  # -> 'Peach'
# print(next(result))  # -> 'Lemon'
# print(next(result))  # ?
print('one else?')
# print(next(result))  # ?
result = to_upper(fruits)
for el in result:
    print(el)
