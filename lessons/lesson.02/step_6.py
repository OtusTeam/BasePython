fruits = ['apple', 'peach', 'lemon']
fruits_upper = []
for fruit in fruits:
    if fruit.startswith('a'):
        continue
    fruits_upper.append(fruit.upper())

print(fruits_upper)
# fruits_upper_2 = [fruit.upper() for fruit in fruits if not fruit.startswith('a')]
fruits_upper_2 = [fruit.upper()
                  for fruit in fruits
                  if not fruit.startswith('a')]
print(fruits_upper_2)
