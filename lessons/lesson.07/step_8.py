class User:
    def __init__(self, name, age, address=None):
        self.name = name
        self._age = self._set_age(age)
        self.address = address

    @property
    def age(self):  # getter
        return self._age

    @age.setter
    def age(self, value):
        self._age = self._set_age(value)

    def _set_age(self, value):
        _age = int(value)
        if _age <= 0:
            raise ValueError('wrong age')

        self._age = _age

    def set_older(self):
        self._age += 1


user_1 = User('Ivan', '25')

print(user_1.age)

# user_1.age = '27'
user_1.age = '-1'
# user_1.age = '27 years'
print(user_1.age)
