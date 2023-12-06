# fruits = ['apple', 'peach', 'lemon']  # memory O(n)
fruits = {'apple', 'peach', 'lemon'}  # memory O(n)

print('potato' in fruits)  # O(n) -> O(1)

fruits_to_check = ['potato', 'tomato']
# for _ in range(1000):  # O(n^2) -> O(n)
for fruit in fruits_to_check:  # O(n^2)
    print(fruit in fruits)

