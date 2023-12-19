class User:
    def __init__(self, username):
        self.username = username
        self.__password = None

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        # magic hash
        self.__password = hash(value)


class Manager(User):
    pass


def main():
    bob = User("bob")
    print(bob.username)
    # print(bob.password)
    # print(bob.__password)
    bob.password = "abc"
    # print(bob.__password)
    print(bob.password)
    print(bob.__dict__)

    bob.__password = 123
    print(bob.__password)
    print(bob.password)
    print(bob._User__password)
    print(bob.__dict__)

    alice = Manager("alice")
    alice.password = "qwe"
    print(alice)
    print(alice.password)
    print(alice._User__password)
    print(alice.__dict__)


main()
