from sys import getsizeof

a = 15
print(type(a), getsizeof(a))

b = 15.0
print(type(b), getsizeof(b))

c = 'hello'

d = False
print(type(d))
# a == b  1 == "1"
# a === b 1 != "1"
print(15 == "15")
print(int(15) == int("15"))
print(str(15) == str("15"))

