# map, filter, zip

fruits = ['apple', 'peach', 'lemon']
fruits_upper = []
for fruit in fruits:
    fruits_upper.append(fruit.upper())

print(fruits_upper)

# fruits_upper_2 = list(map(str.upper, fruits))  # memory O(n)
fruits_upper_2 = map(str.upper, fruits)  # memory O(1)
print(fruits_upper_2)

for el in fruits_upper_2:
    print(el)

for el in fruits_upper_2:
    print(el)

