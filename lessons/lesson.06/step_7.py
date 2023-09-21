class TooYoungUser(Exception):
    pass


def _age_validator(age):
    age = int(age)
    if age < 21:
        raise TooYoungUser('too young', age)
    return age


class User:
    def __init__(self, name, age=None):
        self.name = name
        self._age = None  # protected
        self.age = age
        self.address = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, val):
        self._age = _age_validator(val)

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}, {self.age} years'

    def __len__(self):
        return len(self.name)

    # def __repr__(self):
    #     pass


class YoungUser(User):
    def _age_validator(self, age):
        age = int(age)
        if age < 18:
            raise TooYoungUser('too young', age)
            # return 'too young'
        return age


try:
    user_1 = User(name='Ivan', age=25)
    # user_1 = YoungUser(name='Ivan', age=18)
except Exception as e:
    print(type(e), e.args)
    print(f'age is {e.args[1]}')
else:
    print(user_1)
    # print(str(user_1))
    print(len(user_1))
