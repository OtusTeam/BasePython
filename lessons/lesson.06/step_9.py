class TooYoungUser(Exception):
    pass


class User:
    MIN_AGE = 25

    def __init__(self, name, age=None, birth_year=None):
        self.name = name
        self._age = None  # protected
        self.age = age
        self.birth_year = birth_year and self._to_int(birth_year) or None
        self.__address = None  # name mangling, private

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, val):
        self._age = self._age_validator(val)

    @staticmethod
    def _to_int(val):
        return int(val)

    @property
    def address(self):
        return self.__address

    @classmethod
    def _age_validator(cls, age):
        # age = int(age)
        age = cls._to_int(age)
        if age < cls.MIN_AGE:
            raise TooYoungUser('too young', age)
        return age

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}, {self.age} years'

    def __len__(self):
        return len(self.name)


class YoungUser(User):
    MIN_AGE = 18


try:
    # user_1 = User(name='Ivan', age=18)
    user_1 = YoungUser(name='Ivan', age=18)
    print(user_1.address)
    # user_1.__address = 'Moscow'
    user_1._User__address = 'Moscow'
    print(user_1.address)
except Exception as e:
    print(type(e), e.args)
    print(f'age is {e.args[1]}')
else:
    print(user_1)
    # print(str(user_1))
    print(len(user_1))
    print(vars(user_1))
