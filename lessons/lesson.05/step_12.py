class User:
    def __init__(self, name, age):
        self.name = name
        # self.age = age
        self._age_setter(age)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        # self._age = int(age)
        self._age_setter(age)

    def _age_setter(self, age):
        self._age = int(age)

    def year_older(self):
        self._age += 1


user_1 = User('Ivan', '25')

print(user_1.age)
user_1.name = 'Boris'
# user_1.age = '25 years'
user_1.age = '25'
user_1.year_older()
user_1.year_older()
user_1.year_older()
print(user_1.age)
print(user_1.name)
