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


class DatabaseException(Exception):
    pass


class NotFountError(DatabaseException):
    pass


class UserNotFound(NotFountError):
    pass


class ArticleNotFound(NotFountError):
    pass


print(NotFountError.mro())
print(UserNotFound.mro())
print(ArticleNotFound.mro())
