class VehicleBase:
    def __init__(self, color):
        self.color = color

    def make_sound(self):
        print("no sound yet")


class Car(VehicleBase):
    def __init__(self, color, wheels):
        self.color = color
        self.wheels = wheels

    def make_sound(self):
        print("beeeeep")

    def open_trunk(self):
        print("opened trunk...")


class Ship(VehicleBase):
    def __init__(self, color, cabins):
        self.color = color
        self.cabins = cabins

    def make_sound(self):
        print("booop")

    def set_sail(self):
        print("set sail done!")


# class Amphibian(Ship, Car):
class Amphibian(Car, Ship):
    def __init__(self, color, wheels):
        # Ship.__init__(self, color, 0)
        # Car.__init__(self, color, wheels)
        self.cabins = 0
        self.color = color
        self.wheels = wheels

    def toggle_mode(self):
        print("toggled mode.")


# car = Car("black", 4)
# print(car.color, "car with", car.wheels, "wheels")
# car.make_sound()
# car.open_trunk()
#
# ship = Ship("white", 5)
# print(ship.color, "ship with", ship.cabins, "cabins")
# ship.make_sound()
# ship.set_sail()


amphibian = Amphibian("green", 4)
print(amphibian)
print(amphibian.__init__)
print(amphibian.color, "amphibian with", amphibian.wheels, "wheels and", amphibian.cabins, "cabins")
amphibian.make_sound()
amphibian.toggle_mode()
amphibian.set_sail()
amphibian.open_trunk()
print(Amphibian.__mro__)
