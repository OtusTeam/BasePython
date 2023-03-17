class User:
    def __init__(self, name, age):
        self.name = name
        self._age_setter(age)
        self._bio = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age_setter(age)

    def _age_setter(self, age):
        self._age = int(age)

    @property
    def bio(self):
        if self._bio is None:
            self._bio = ...
        return self._bio

    def year_older(self):
        self._age += 1


class AdminUser:
    def __init__(self, name, age, access_level):
        self.name = name
        self._age_setter(age)
        self._bio = None
        self.access_level = access_level

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age_setter(age)

    def _age_setter(self, age):
        self._age = int(age)

    @property
    def bio(self):
        if self._bio is None:
            self._bio = ...
        return self._bio

    def year_older(self):
        self._age += 1


user_1 = User('Ivan', '25')
user_2 = AdminUser('Boris', 35, 'admin')
print(user_1.age)
print(user_2.age)

