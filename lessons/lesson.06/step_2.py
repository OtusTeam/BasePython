from step_0 import Point


def add(a, b):
    return a + b
    # return str(a) + str(b)


print(add("foo", "bar"))
print(add(1, 2))
print(add([3, 4], [1, 2]))
print(add(Point(1, 2), Point(3, 4)))


# add(1, "2")

# a = 3
# b = "2"
# c = add(a, b)
# print("hello")
# d = c / 2
# print(c)
# print(d)

# raise TypeError("invalid type")
raise Exception("вы неправы")
print("hello")
