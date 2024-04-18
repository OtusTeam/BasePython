fruits = ['apple', 'peach', 'lemon']

print(fruits)
# fruits_gen = (el.title() for el in fruits)
fruits_iter = map(str.title, fruits)  # O(1) memory
# print(type(fruits_iter))
# print(dir(fruits_iter))
# for el in fruits:...

for el in fruits_iter:
    print(el)
