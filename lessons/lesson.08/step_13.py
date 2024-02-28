class User:
    MIN_AGE = 18

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self._age = self._clear_age(age)

    @classmethod
    def create_caps(cls, first_name, last_name, age):
        return cls(first_name.upper(), last_name.upper(), age)

    @classmethod
    def _clear_age(cls, value):
        value = int(value)
        if value < cls.MIN_AGE:
            raise ValueError('age is too small')

        return value

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name} ({self._age})"

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = self._clear_age(value)

    def inc_age(self):
        self._age += 1

    def __str__(self):
        return (
            f'{self.__class__.__name__}: {self.full_name} '
            f'(min age {self.MIN_AGE})'
        )


class CustomUser(User):
    pass


class Users:
    def __init__(self):
        self._items = []

    def add(self, item):
        self._items.append(item)

    def __contains__(self, item):
        return item in self._items  # O(n)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)


user_1 = User("John", "Doe", '18')
user_2 = CustomUser("Ivan", "Ivanov", '28')
user_3 = User("Boris", "Borisov", 31)
otus_users = Users()
otus_users.add(user_1)
otus_users.add(user_2)

# c = 1 + 5

print(user_1 in otus_users)
print(user_3 in otus_users)
print(len(otus_users))

for el in otus_users:
    print(el)
