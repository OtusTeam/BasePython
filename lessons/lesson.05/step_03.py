

class UserType:
    USER = "user"
    MANAGER = "manager"
    ADMIN = "admin"

    @classmethod
    def get_all(cls):
        return [
            cls.USER,
            cls.MANAGER,
            cls.ADMIN,
        ]

# who calls - C
# method - M
# C.M() -> C.M(C)


print(UserType.ADMIN)
print(UserType.get_all())


class User:
    # инициализатор != конструктор
    def __init__(self, name: str):
        self.name = name
        self.age = 0

    # конструктор (можно так называть)
    # def __new__(cls, *args, **kwargs):
    #     pass


user_sam = User(name="sam")
print(user_sam)
print(user_sam.__dict__)

user_john = User("john")
print(user_john.__dict__)
print(user_john.name)
print(user_john.age)
