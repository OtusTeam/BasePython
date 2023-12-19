def final_call():
    print("done processing, returning result")
    1 / 0


def final_call_safe():
    try:
        final_call()
    except ZeroDivisionError:
        print("final call error")


def div_safe(a, b):
    try:
        result = a / b
        if result == 1:
            print("result is one")

        # return result
    # except (TypeError, ZeroDivisionError):
    except TypeError:
        print("!!please use only numbers")
    except ZeroDivisionError:
        print("please don't divide by zero")
        # return 0
        return float("inf")
    except ArithmeticError:
        print("some arithmetic error!")
    else:
        print("ok div, return", result)
        return result
    finally:
        final_call_safe()

    return float("-inf")


def main():
    print(div_safe(10, 2))
    print(div_safe(10, 4))
    print(div_safe(10, ""))
    print(div_safe(8, 6))
    print(div_safe(8, 0))
    print(div_safe(10, 5))


main()


def get_user_from_db(db_url, username: str):
    db = DB(db_url)

    try:
        return db.get_user(username)
    # except UserNotFoundError:
    #     pass
    # except DbConnectionError:
    #     pass
    finally:
        db.close_connection()
