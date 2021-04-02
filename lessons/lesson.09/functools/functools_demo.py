from functools import wraps, partial

def trace(func):
    func.level = 0
    @wraps(func)
    def inner(*args, **kwargs):
        args_str = ', '.join(map(str, args))
        print(f"{func.level} --> {func.__name__}({args_str})")
        func.level -= 1
        res = func(*args, **kwargs)
        print(f"{func.level} <-- {func.__name__}({args_str}) = {res}")
        return res
    return inner

@trace
def is_even(n):
    if n % 2 == 0:
        return True
    return False


# A normal function
def add(a, b, c):
    return 100 * a + 10 * b + c


# A partial function with b = 1 and c = 2
add_part = partial(add, c=2, b=1)

# Calling partial function
print(add_part(3))


print(is_even(4))
