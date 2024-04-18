def to_upper(items):
    for el in items:
        yield el.title()


fruits = ['apple', 'peach', 'lemon']

print(fruits)
fruits_gen = to_upper(fruits)
print(type(fruits_gen))
print(dir(fruits_gen))
# iterator -> next(...), StopIteration
# iterator -> generator
# fruits_gen.send('new value')
# fruits_gen.throw(ValueError)
# fruits_gen.close()
