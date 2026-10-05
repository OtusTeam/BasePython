def divide_verbose(a, b):
    print(a, "/", b)
    result = 2.0**2000
    result = a / b
    print("=", result)
    return result


def main():
    try:
        res = divide_verbose(10, 0)
    except ZeroDivisionError:
        print("don't divide by zero please")
    except ArithmeticError as e:
        print("ArithmeticError:", e, type(e))
    except TypeError:
        print("only numeric please")
    else:
        print("res:", res)
        print("x10:", res * 10)

    print("finish")


if __name__ == "__main__":
    main()
