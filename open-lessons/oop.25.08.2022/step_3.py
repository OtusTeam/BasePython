class MyError(Exception):
    pass


print(MyError, MyError.mro())

raise MyError("this is an error")
