import sys
# vars a: integer;
a = 15
print(type(a), id(a), sys.getsizeof(a))

a = 15.0
print(type(a), id(a), sys.getsizeof(a))

a = '15'
print(type(a), id(a), sys.getsizeof(a))

a = True
print(type(a), id(a), sys.getsizeof(a))
