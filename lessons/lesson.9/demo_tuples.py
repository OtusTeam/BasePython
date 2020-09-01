t1 = 1, 2
t2 = (1, 2)

assert t1 == t2

a = 7
b = 3

a, b = b, a

print(a, b)


def func():
    return 42, 7


res = func()
print(res)

r1, r2 = res
print(r1, r2)

j, k = func()
print(j, k)
