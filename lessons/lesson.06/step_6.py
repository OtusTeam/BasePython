class User:
    def __init__(self, name):
        self.name = name
        self._password = None


john = User(name="John")
print(john.name)
print(john._password)

john._password = 'pwd'
print(john._password)
print(john.__dict__)


class User:
    def __init__(self, name):
        self.name = name
        self.__password = None


class Manager(User):
    pass


sam = User(name="Sam")
print(sam.name)
print(sam.__dict__)
print(sam._User__password)
sam._User__password = "abc"
print(sam._User__password)

# print(sam.__password)
# print(sam._password)

manager = Manager(name="nick")
print(manager.__dict__)
print(manager._User__password)
manager._User__password = "man"
print(manager._User__password)
