class Car:
    def __init__(self, doors, sound):
        self.doors = doors
        self.sound = sound

    def make_sound(self):
        print("car with", self.doors, "doors does", self.sound)


class RaceCar(Car):
    ...


class Ship:
    def __init__(self, cabins, sound):
        self.cabins = cabins
        self.sound = sound

    def make_sound(self):
        print("ship with", self.cabins, "cabins does", self.sound)


class Yach(Ship):
    ...


# class Amphibian(Car, Ship):
class Amphibian(Ship, Car):
    def __init__(self, doors, cabins, sound, color):
        Car.__init__(self, doors, sound)
        Ship.__init__(self, cabins, sound)
        self.color = color

    def make_sound(self):
        print(
            "Amphibian with",
            self.doors,
            "doors and",
            self.cabins,
            "cabins and color",
            self.color,
            "makes sound",
            self.sound,
        )


print(Amphibian.mro())

amph = Amphibian(doors=4, cabins=1, sound="boop", color="green")
print(amph.doors)
print(amph.sound)
print(amph.cabins)
print(amph.color)
amph.make_sound()
