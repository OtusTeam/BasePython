class User:
    def __init__(self, name: str):
        self.name = name
        # self.password = None
        self.__password = None

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        # self.__password = hash(value)
        self.set_password(value)

    def set_password(self, new_password):
        """
        # >>> hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        # <<< "salt$100000$hash"

        # bcrypt.checkpw(password, hashed):
        # salt, iters, hashed_pw = hashed.split("$")
        # ... bcrypt.hashpw(password, salt, iters=iters..)

        :param new_password:
        :return:
        """
        self.__password = hash(new_password)

    def password_valid(self, password) -> bool:
        # return hash(password) == self.password
        return hash(password) == self.__password


user = User("john")
user.password = "qwerty1234"
# user.set_password("qwerty1234")

user.__password = 'qwerty'
# name mangling
print(user.__dict__)
print(user, [user.name, user.password, user._User__password])
# print(user, [user.name, user.password()])

# print(user.password_valid)
print(user.password_valid("qwerty"))
print(user.password_valid("qwerty1234"))
