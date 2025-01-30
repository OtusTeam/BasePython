from functools import partial


def power(base, exponent):
    return base ** exponent


square = partial(power, exponent=2, base=3)
result = square()
print(f"в квадрате = {result}")