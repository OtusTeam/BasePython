# default = object()


def div_safe(a, b):
    try:
        result = a / b
        if result == 1:
            print("ret 1")
            return result
    except TypeError:
        print("please use numbers")
    except ZeroDivisionError:
        print("pls don't divide by zero")
        # return 0
        return float("inf")
    except ArithmeticError:
        print("arithm err")
    else:
        print("return result", result)
        return result
    finally:
        print("done processing div", [a, b])

    print("return default result")
    # return default


print(div_safe(10, 4))
print(div_safe(10, "1"))
print(div_safe(10, 5))
print(div_safe(10, 0))
print(div_safe(10, 10))


def write_to_file(filename: str, text: str):
    file = open(filename)
    try:
        file.write(text)
    # except FileWriteError:
    #     print(...)
    finally:
        file.close()


def get_user(db_url, username: str):
    db = DB(db_url)
    try:
        return db.get_user(username)
    # except UserNotFound:
    #     pass
    # except DbError:
    #     pass
    finally:
        db.close_connection()
