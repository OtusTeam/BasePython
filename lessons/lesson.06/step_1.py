
# noresult = object()


def add_safe(a, b):
    try:
        return a + b
    except TypeError:
        print("caught type error")
        # return noresult
        # return None


print(add_safe(2, 3))
print("res none:", add_safe(2, "3"))
print(add_safe(4, 3))
print("end")
