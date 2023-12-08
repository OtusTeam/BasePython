def sum_squares(x, *args):
    print(x, args)
    return sum(el ** 2 for el in args)


print(sum_squares(2, 3))
print(sum_squares(2, 3, 5))

# a = 5
# b = 7
# # a, b = b, a
# # c = b, a
# # a, *b = b,
# # a, *b = b, a, b, a
# # a, *b = b, a, b
# # a, *b = b, a
# a, *b = b,
# print(a, b)
# # print(c)
