# def sum_it(a, b, c=0, d=0):
#     return a + b + c + d

def sum_it(*args):
    print(args)
    # return sum(args)
    result = 0
    for el in args:
        result += el
    return result
    # print('never')


print(sum_it(1, 5))
print(sum_it(1, 5, 7))
print(sum_it(1, 5, 7, 14))
print(sum_it(1, 5, 7, 14, 18))
