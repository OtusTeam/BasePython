



def div_safe(a, b):
    print("start for", [a, b])
    try:
        c = a / b
    # except (TypeError, ZeroDivisionError) as e:
    # except Exception:
    #     pass
    except TypeError as e:
        # print("ooops", e, repr(e))
        print("ooops", e)
        # return None
    # except ArithmeticError:
    #     pass
    except ZeroDivisionError:
        print("please don't divide by zero!")
        return 0
    # except ArithmeticError:
    #     pass
    # except ValueError:
    #     pass
    # except NameError:
    #     pass
    # except Exception:
    #     pass
    else:
        print("- return c")
        return c
    finally:
        print("finally for", [a, b])

    print("leaving with", [a, b])


print(div_safe(1, 2))
print(div_safe(10, 2))
print(div_safe(10, 3))
print(div_safe(10, "2"))
print(div_safe(12, 4))
print(div_safe(1, 0))
print(div_safe("1", 0))
print(div_safe(123, 5))

# try:
#     conn.send_data()
# finally:
#     conn.close()

# try:
#     1/0
# except ValueError:
#     pass
# else:
#     print("ok")
