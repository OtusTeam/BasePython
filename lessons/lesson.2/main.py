"""
Lesson about funcs
iterators, generators, comprehensions
"""

from operator import mul
from time import time
from functools import wraps, reduce


def secondary():
    print("Secondary")


def add(a, b):
    # return a + b
    print("Add", a, b)
    res = a + b
    print("Result:", res)
    return res


def div(a, b):
    """
    Divide a by b

    :param a:
    :param b:
    :return:
    """
    if b == 0:
        return
    return a / b


def rain_today():
    res = ...  # some web request to weather API
    if res.status == "OK":
        return res.data.will_rain  # True/False
    # print("status not ok")
    return None


def demo_lines():
    multiline = """Zero line
    First line
    Second line
    12345678'''''"asd""
    """

    online = "line1\nline2"

    print(multiline)
    print(online)


def greet(name="World"):
    print("Hello", name)


def multiply_lines(input_line, times, lines=None):
    if lines is None:
        lines = {}
        print('id of dict:', id(lines))
    for i in range(1, times + 1):
        lines[i] = input_line * i
    return lines


def power(a, p=2):
    return a ** p


def count_values(counter, *args, as_list=False):
    print(counter)
    print(args)
    if as_list:
        # l = []
        # for v in args:
        #     l.append(counter(v))
        # return l
        return [counter(v) for v in args]

    # d = {}
    # for v in args:
    #     d[v] = counter(v)
    # return d
    return {v: counter(v) for v in args}


def my_range(start, end=None, step=1):
    """
    :param start:
    :param end:
    :return:
    """
    if end is None:
        end = start
        start = 0

    print("entering cycle")
    while start < end:
        print("yielding", start)
        yield start
        # v = v + step
        start += step
        print("increased v to", start)


def main():
    # secondary()
    print("Hello main!")
    # secondary()
    # add(5, 3)
    # div_res = div(10, 2)
    # print("div_res 2:", div_res)
    # div_res = div(10, 0)
    # print("div_res 0:", div_res)
    greet("John")
    greet()
    lines = multiply_lines('foo', 5)
    print('id of returned dict:', id(lines))

    print(lines)
    print(multiply_lines('spam', 4, lines))
    print(multiply_lines('spam and eggs', 2))

    res = count_values(power, 1, 2, 3, 4, 5, 6)
    print(res)
    res = count_values(power, 1, 2, 3, 4, 5, 6, 7, 8, 9, as_list=True)
    print(res)

    r = range(10)
    print(r)
    print(list(r))
    print(tuple(r))
    for i in r:
        print(i, end=" ")
    print()
    s = {v for v in r}
    s.add(7)
    print(s)
    t = (power(v, 3) for v in r)
    print(t)
    print('first', next(t))
    print('second', next(t))
    for i in t:
        print(i)

    range_g = my_range(10)
    print(range_g)
    print("next val:", next(range_g))
    print("first next done")
    print("doing next again")
    print("next val:", next(range_g))
    print("doing next again 2")
    print("next val:", next(range_g))
    print(list(range_g))


def time_func(func, *args):
    print("timing func", func, "with args", args)
    start_time = time()
    print("time before", start_time)
    res = func(*args)
    end_time = time()
    print("time after", end_time)
    print("computed in", end_time - start_time)
    print("returning result", res)
    return res


def timing_dec(func):
    print("entering decorator with", func)

    @wraps(func)
    def wrapper(*args):
        return time_func(func, *args)

    print("returning decorated")
    return wrapper

def demo_wo_decorators():
    res = time_func(power, 10_000_000_000, 1_000)
    print("got res", res)

    res = time_func(power, 10_000_000_000_000_000_000_000_000_000_000)
    print("got res", res)

    res = time_func(div, 1000, 20)
    print("got res", res)



# main()

# demo_wo_decorators()

# demo decorators

@timing_dec
def new_power(a, p=2):
    return a ** p

# new_power = timing_dec(new_power)

# print('new_power name', new_power.__name__)


# new_div = timing_dec(div)

# print(new_power(10_0000000000000000000000000000))
# print(new_div(100, 2))


#
#
#
#

values = list(range(10))
print("values", values)
powered_gen = map(new_power, values)
print("powered gen", powered_gen)
print("res", list(powered_gen))

# def my_func(v):
#     return v % 2 == 0


only_even = filter(lambda v: v % 2 == 0, values)
print("only even gen", only_even)
print("only even:", list(only_even))

print(sum(values))

values_to_mul = values[1:]
print("values_to_mul", values_to_mul)

res = 1
for v in values_to_mul:
    res *= v

print("res", res)

res = reduce(mul, values_to_mul)
print("reduce result:", res)


def accept_kwargs(**kwargs):
    print(kwargs)


accept_kwargs(foo="bar", spam="eggs", baz=123)
