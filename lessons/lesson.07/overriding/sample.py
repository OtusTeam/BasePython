class SuperUser:
    def super_test(self):
        print('I am a super user')


class User(SuperUser):

    # overloading - перегрузка
    def test(self):
        print('I am a user')

    def test(self, name, surname):
        print('Overriding')

    def test(self, name, surname, age):
        print('Overriding again')

    # overriding - переопределение
    def super_test(self, name):
        print('I am a child user: {}'.format(name))

    def super_test(self):
        print('I am a child user')


user = User()
# user.test()
# user.test('Nigar', 'Movsumova')
user.test('Nigar', 'Movsumova', 26)
user.super_test('Nigar')
user.super_test()
