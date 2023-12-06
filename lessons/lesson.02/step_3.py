fruits = ['apple', 'peach', 'lemon']
# for fruit in fruits:
#     print('this is', fruit)

for idx, fruit in enumerate(fruits, 1):
    print(idx, 'this is', fruit)

i = 0
fruits_len = len(fruits)
while i < fruits_len:
    print(i + 1, 'this is', fruits[i])
    i += 1

# for i in range(len(fruits)):
#     print(i + 1, 'this is', fruits[i])
