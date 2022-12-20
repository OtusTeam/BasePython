

def div_safe(a, b):
    print("start for", [a, b])

    try:
        c = a / b
        # return a / b
    except TypeError as e:
        print("oops, type error:", e, repr(e))
    except (NameError, ValueError) as e:
        print("err", e)

    except ZeroDivisionError:
        print("please don't divide by zero")
        return 0

    else:
        print("- return c", c)
        return c

    finally:
        print("finally for", [a, b])

    # except ArithmeticError as e:
    #     print("a e", e)

    print("leaving for", [a, b])

    # return c

print(div_safe(1, 2))
print(div_safe(10, 2))
print(div_safe(10, "3"))
print(div_safe(10, 5))
print(div_safe(10, 0))
