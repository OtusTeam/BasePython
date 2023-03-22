def div(a, b):
    return a / b


for i in range(2):
    if i == 2:
        break
    print(i)
else:
    print("done. no break")


def div_safe(a, b):
    try:
        result = div(a, b)
        # return div(a, b)
    except TypeError as e:
        print("could not divide, type error", e)
    except ZeroDivisionError:
        print("please don't divide by zero!")
        return 0
    # except ArithmeticError:
    #     print("ArithmeticError")
    # except Exception as e:
    #     pass
    else:
        print("else ok, return result")
        return result
    finally:
        print("finally for", [a, b])

    print("leaving at the end")
    return None


print(div_safe(10, 2))
print(div_safe(10, "2"))
print(div_safe(10, 4))
print(div_safe(10, 0))
print(div_safe(10, 5))

