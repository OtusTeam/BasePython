class User:
    MIN_AGE = 21

    __slots__ = ('name', 'age', 'address')

    def __init__(self, name, age=None):
        self.name = name
        self.age = age
        self.address = None


user_1 = User(name='Ivan')
user_1.skill = 'junior'
print(vars(user_1))
print(user_1.__dict__)
