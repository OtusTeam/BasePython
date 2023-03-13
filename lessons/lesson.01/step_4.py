import sys

a = [15, 85.2, 'hello']
print(a, id(a))
a.append(55)
print(a, id(a))

b = (15, 85.2, 'hello')
b.append(55)

