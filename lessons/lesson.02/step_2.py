fruits = ['apple', 'peach', 'lemon']
fruits_as_set = set(fruits)

fruits_to_check = ['potato', 'tomato']

for fruit in fruits_to_check:
    print(fruit in fruits)
