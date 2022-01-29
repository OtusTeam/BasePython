class ColorMixin:

    def get_color(self):
        return ""


class Animal(ColorMixin):
    pass


class Cat(Animal):
    def get_color(self):
        return "Black"


class Dog(Animal):
    def get_color(self):
        return "Gray"


class Car(ColorMixin):
    def get_color(self):
        return "Red"
