class User:
    def __init__(self, name: str):
        self.name = name
        # self._count = 0
        self.__password = None

    @property
    def password(self):
        # self._count
        return self.__password

    @password.setter
    def password(self, value):
        # TODO: real secure hashing
        self.__password = hash(value)


bob = User("Bob")
print(bob.name)
print(bob.password)
bob.password = "pwd"
print(bob.password)
bob.password = "secure"
print(bob.password)
bob.password = "pwd"
print(bob.password)
