def div_safe(a, b):
    try:
        # raise OverflowError
        # return a / b
        c = a / b
    except ZeroDivisionError:
        print("pls don't divide by zero")
        return 42
    except TypeError as e:
        print("oops", e)
        # return
    else:
        return c
    finally:
        print("finally for", [a, b])

    print("leaving func for", [a, b])


print(div_safe(3, 4))
print(div_safe(10, 2))
print(div_safe(10, 0))
print(div_safe(2, 3))
print(div_safe(2, "3"))
print(div_safe(3, 1))


def get_user(username):
    # db = object()
    db = init_db()
    try:
        user = db.get_user(username)
        return user
    except DataBaseError:
        log.error("could not fetch user %s", username)
    # else:
    #     return user
    finally:
        db.close_connection()

# get_user("username")

try:
    raise ValueError("hello")
except ValueError as e:
    print(repr(e))

print(repr(ValueError("hello")))
