a = 4
b = 'hello'
c = 45.7
print(a, b, c)

a, b, c = b, c, a
a, *b = b, c, a
d = b, c, a

print(a, b, c)
print(type(d), len(d))
print(d)
# return user,
