# Создать класс User со следующими атрибутами:
# имя, фамилия, почтовый адрес, мобильный номер, пароль
# Создать геттер и сеттер для пароля.
# Переопределить магический метод __str__, чтобы он более визуально правильно выводил информацию о юзере.
# Исключите из __str__ информацию о пароле пользователя.
# Создайте класс Pet и добавьте к нему следующие атрибуты:
# кличка, порода, год рождения, хозяин (User)
# Добавьте список из объектов как атрибут экземпляра для User.
# Создайте несколько экземпляров класса User, добавьте к юзерам 1-4 домашних животных


class User:

    def __init__(self, name, surname, address, number, password, pets=[]):
        self.name = name
        self.surname = surname
        self.address = address
        self.number = number
        self.__password = password
        self.pets = pets

    def __str__(self):
        return f'{self.name} {self.surname}, ' \
               f'address: {self.address}, ' \
               f'number: {self.number}, ' \
               f'pets: {self.pets}'


    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, password):
        self.__password = password

    @password.getter
    def password(self):
        return self.password


class Pet:
    def __init__(self, name, breed, type, birth_year, owner=None):
        self.name = name
        self.breed = breed
        self.type = type
        self.birth_year = birth_year
        self.owner = owner

    def __str__(self):
        return f'{self.name}, ' \
               f'type: {self.type}, ' \
               f'breed: {self.breed}, ' \
               f'birth_year: {self.birth_year},'\
               f'\nowner: {self.owner}'


owner = User('Nigar', 'Movsumova', 'Baku, Azerbaijan', '+994xxxxxxxxx', '1234')
cat = Pet('Richard', 'Scottish Straight', 'Cat', '2020')
owner.pets.append(cat)
cat.owner = owner

print(owner)
print(cat)


