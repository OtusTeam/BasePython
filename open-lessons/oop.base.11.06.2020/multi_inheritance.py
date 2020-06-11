class A:
    def a(self):
        return "A"


class B:
    def b(self):
        return "B"


class C:
    def c(self):
        return "C"


class MyMixin():
    def __init__(self):
        self.__value = 40
        self.__value_square = 0
        self.update_square()

    def update_square(self):
        self.__value_square = self.value ** 2

    @property
    def value_square(self):
        return self.__value_square

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, v):
        if v < 0:
            raise Exception("Value has to be 0 or greater")
        self.__value = v
        self.update_square()


class MyClass(A, B, C, MyMixin):
    def method(self):
        return " ".join((self.a(), self.b(), self.c()))


if __name__ == '__main__':
    print(MyClass.__mro__)
    my_cls = MyClass()
    print(my_cls.method())

    print("value", my_cls.value)
    print("square", my_cls.value_square)
    print("set value to 30")
    my_cls.value = 30
    print("now value", my_cls.value)
    print("now value square", my_cls.value_square)
