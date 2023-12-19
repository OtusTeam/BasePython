no_result = object()


def add_safe(a, b):
    try:
        # return pow(a, b)
        return a + b
    except TypeError:
        print("caught a type error")
        # return "no result"
        # return no_result
        # return None


def main():
    res = add_safe(1, 2)
    print("res:", res)
    res = add_safe("3", 1)
    if res is no_result:
        print("got no result")
    print("res:", res)
    res = add_safe(3, 4)
    print("res:", res)


main()
