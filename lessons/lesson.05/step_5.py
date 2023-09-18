class User:
    MIN_AGE = 21

    def __init__(self, name, age=None, skill=None):
        self.name = name
        self.age = age
        self._skill = skill
        self.address = None

    @property
    def skill(self):  # getter
        return self._skill


# list VS tuple
user_1 = User(name='Ivan', skill='junior')
print(vars(user_1), id(user_1))
print(user_1.skill)
# print(user_1.skill())
# print(user_1._skill)
# user_1.skill = 'middle'  # immutable
# print(vars(user_1), id(user_1))
