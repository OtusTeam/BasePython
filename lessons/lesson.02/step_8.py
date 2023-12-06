fruits = ['apple', 'peach', 'lemon']


def my_processor(fruit):
    return fruit.upper()


fruits_upper_2 = list(map(my_processor, fruits))  # memory O(n)
print(fruits_upper_2)
