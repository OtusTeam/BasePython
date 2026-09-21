# print(123)
#
#
# my_print = print
#
# print(my_print)
#
# my_print(12345)

def outer(name):
    return print


my_print = outer('ivan')
my_print(123456)