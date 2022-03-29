class User:
    def __init__(self, pk, name, age):
        self.pk = pk
        self.name = name
        self.age = age

    def __str__(self):
        return f'User(pk={self.pk}, name={self.name}, age={self.age})'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__class__ == other.__class__ \
               and self.pk == other.pk


class Book:
    pass


class Car:
    pass


class AdminUser(User):
    pass


user_1 = User(1, 'Ivan', 25)
user_2 = AdminUser(1, 'Ivan', 25)
print(user_1)
print([user_1, user_2])
print(user_1.name)
print(id(user_1), id(user_2))
print(user_1 == user_2)
