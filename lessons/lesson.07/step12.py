import random


def gen_func():
    while True:
        yield random.randint(1, 100)


gen = gen_func()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for i in gen:
    print(i)