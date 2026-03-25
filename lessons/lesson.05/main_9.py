def w(x):
    return x > 17

#
# print(add(1, 2))

#
# add_lambda = lambda x, y: x + y
# print(add_lambda(3, 2))


temp = [18, 10, 9, 23, 32, 17, 12, 15, 22]
# warm = filter(lambda value: value > 17, temp)
warm = filter(w, temp)
print(type(warm))
print(list(warm))

warm = map(lambda value: str(value), temp)
print(type(warm))
print(list(warm))