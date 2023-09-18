class User:
    MIN_AGE = 21

    def __init__(self, name, age=None, skill=None):
        self.name = name
        self.age = age
        self._skill = None
        self.address = None

    @property
    def skill(self):  # getter
        # cache
        if not self._skill:
            return 'undefined'
        return self._skill

    @skill.setter
    def skill(self, val):  # setter
        if len(val) > 6:
            # raise ValueError('skill is too long')
            print('skill is too long')
            return
        self._skill = val


# user_1 = User(name='Ivan', skill='junior')
user_1 = User(name='Ivan')
print(vars(user_1), id(user_1))
print(user_1.skill)
user_1.skill = 'middles'
print(vars(user_1), id(user_1))
print(user_1.skill)
