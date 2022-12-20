a = 5
b = 'hello'
print(a, b)
# a, b = b, a
# (a, b) = (b, a)
[a, b] = [b, a]
print(a, b)

# a, b, c = c, a, b
val_1 = ['hello', 'world']  # id_1
# val_2 = val_1  # -> id_1
val_2 = ['hello', 'world']  # id_2
print(id(val_1), id(val_2))
