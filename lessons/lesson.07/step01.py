# print(123)
#
# my_print = print
#
# print(type(print))
# print(type(my_print))
#
# my_print(12345)

# def outer(name):
#     def inner():
#         print(f' Привет, {name}')
#     return inner
#
#
# hello_name = outer('Bob')
# print(type(hello_name))
# print(hello_name)
#
# hello_name()
# hello_name()
# hello_name()


def make_mul(x):
    def mul(y):
        return x * y
    return mul


mul_by_10 = make_mul(10)
print(mul_by_10)
print(mul_by_10(5))
print(mul_by_10(3))
print(mul_by_10(7))

mul_by_7 = make_mul(7)
print(mul_by_7)
print(mul_by_7(5))
print(mul_by_7(3))
print(mul_by_7(7))

print(mul_by_10(10))