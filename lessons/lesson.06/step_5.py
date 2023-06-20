
try:
    # raise ValueError()
    raise ValueError
except ValueError as ex:
    print(ex, type(ex))

ex_ = ValueError()
print("ex:", ex_)
print("type ex", type(ex_))

print(type(ValueError))

# print(type.mro(type))
