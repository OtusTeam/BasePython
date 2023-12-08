def fruits_upper_gen(items):  # memory O(n)
    result = []
    for el in items:
        result.append(el.upper())
    return result


fruits = ['apple', 'peach', 'lemon']
fruits_upper_2 = map(str.upper, fruits)  # memory O(1)

print(*fruits_upper_2)
print(*fruits_upper_gen(fruits))
