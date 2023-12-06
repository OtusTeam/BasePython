fruits = ['apple', 'peach', 'lemon']
fruits_upper = []
for fruit in fruits:
    fruits_upper.append(fruit.upper())
# list comprehension
print(fruits_upper)
fruits_upper_2 = [fruit.upper() for fruit in fruits]
print(fruits_upper_2)

