def to_upper(items):
    for el in items:
        yield el.title()


fruits = ['apple', 'peach', 'lemon']

fruits_gen = (el.title() for el in fruits)

print(type(fruits_gen))
for el in fruits_gen:
    print(el)
