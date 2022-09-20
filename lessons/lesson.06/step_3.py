class MyError(Exception):
    pass


print(MyError)
print(MyError.mro())
print(repr(MyError("eroror")))


raise MyError
# raise MyError("error text!")
# raise MyError()

print("never")


# try:
#     raise MyError
# except MyError:
#     pass

# try:
#     1/0
# except Exception as e:
#     e_type = type(e)
#
# print("e_type:", e_type)
