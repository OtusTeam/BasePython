def to_upper(items):
    for el in items:
        yield el.title()


fruits = ['apple', 'peach', 'lemon']
# a = ('apple')
# a = 'apple',
# print(type(a))

# print(fruits)
# # fruits_gen = to_upper(fruits)
fruits_set_compr = {el for el in fruits}  # -> set
fruits_compr = [el for el in fruits]  # -> list
fruits_gen = (el for el in fruits)  # -> ?tuple, genexp
# print(type(to_upper))
print(type(fruits_set_compr))
print(type(fruits_compr))
print(type(fruits_gen))
