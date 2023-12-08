def fruits_upper_gen(items):  # memory O(1)
    for el in items:
        # return el.upper()
        yield el.upper()


fruits = ['apple', 'peach', 'lemon']
fruits_upper_2 = map(str.upper, fruits)  # memory O(1)

print(*fruits_upper_2)
print(*fruits_upper_gen(fruits))
