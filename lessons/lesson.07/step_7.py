class User:
    def __init__(self, name):
        self.name = name
        self._password = None


u = User("John")
print(u.name, u._password)
u._password = "spam"
print(u.name, u._password)


class User:
    def __init__(self, name):
        self.name = name
        self.__password = "abc"

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        print("set password =", value)
        self.__password = hash(value)


u = User("John")
print(u.name, u.password)
print(u.__dict__)
print(u.name, u._User__password)

u.__password = "sb"
print(u.name, u._User__password)
print(u.name, u.password)

print(u.__dict__)


class Manager(User):
    pass

m1 = Manager("admin")
print(m1.name, m1.password)
print(m1.__dict__)
print(m1.__class__)
print(m1.name, m1._User__password)

m1.password = "qwerty"
print(m1.name, m1.password)
print(m1.name, m1._User__password)
print(m1.__dict__)
