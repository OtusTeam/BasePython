import sys

a = [15, 85.2, 'hello']
print(type(a), id(a), sys.getsizeof(a))

print(a[0], a[-1], a[len(a) - 1])

