class MyError(Exception):
    pass


print(MyError, MyError.mro())

err = MyError("some text")
print("hello")
print("exc", err, repr(err))
print("bye!")

# raise err
# raise MyError
# raise MyError()
raise MyError("erroro")
print("never")




