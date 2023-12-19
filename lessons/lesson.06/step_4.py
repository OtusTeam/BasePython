print(Exception)
print(type(Exception))
print(Exception.mro())

print(ValueError)
print(ValueError.mro())

print(ZeroDivisionError)
print(ZeroDivisionError.mro())


class MyError(Exception):
    pass


print(MyError)
print(MyError.mro())


class DbException(MyError):
    pass


print(DbException)
print(DbException.mro())


class NotFoundError(DbException):
    pass


class UserNotFoundError(NotFoundError):
    pass


class PostNotFoundError(NotFoundError):
    pass
