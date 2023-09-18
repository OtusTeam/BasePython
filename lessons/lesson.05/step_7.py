class User:
    MIN_AGE = 21

    def __init__(self, name, age=None):
        self.name = name
        self._age = None
        self.age = age
        self.address = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, val):
        if int(val) < self.MIN_AGE:
            print('too young')
            return
        self._age = val


class YoungUser(User):
    MIN_AGE = 18


# user_1 = User(name='Ivan', age=15)
user_1 = YoungUser(name='Ivan', age=18)
# print(vars(User), id(User))
# print(vars(user_1), id(user_1))
print(vars(user_1))
print(user_1.age)
print(isinstance(user_1, YoungUser))
print(isinstance(user_1, User))
print(issubclass(YoungUser, User))
print(issubclass(User, YoungUser))
