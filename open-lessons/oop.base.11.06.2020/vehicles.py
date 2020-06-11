class BaseVehicle:
    def make_sound(self):
        raise NotImplementedError


class Car(BaseVehicle):
    SOUND = "beep!"
    CONSUMPTION = 10

    def __init__(self, fuel: int, doors: int = 5, wheels: int = 4):
        """
        :param fuel:
        :param doors:
        :param wheels:
        """
        self.__fuel = fuel
        self.__doors = doors
        self.__wheels = wheels

    def __str__(self):
        return f"{self.__class__.__name__}. fuel: {self.__fuel}, doors: {self.__doors}, wheels: {self.__wheels}"

    @property
    def fuel(self):
        return self.__fuel

    def make_sound(self):
        print(self.SOUND)
        return self.SOUND

    def drive(self, distance: int):
        to_spend = self.CONSUMPTION * distance
        if self.__fuel < to_spend:
            raise Exception("Not enough fuel!")
        self.__fuel -= to_spend
        print(f"Drive {distance}, spend: {to_spend}, fuel left: {self.__fuel}")
        return self.__fuel

    def add_fuel(self, amount: int):
        self.__fuel += amount
        print(f"Added {amount}, left {self.__fuel}")
        return self.__fuel


class SportCar(Car):
    SOUND = "beep beep!!"
    CONSUMPTION = 30

    def __init__(
        self,
        fuel: int,
        doors: int = 2,
        wheels: int = 4,
        doors_open_upwards: bool = True,
    ):
        super().__init__(fuel, doors, wheels)
        self.doors_open_upwards = doors_open_upwards


def drive_by_car(car: Car, distance: int):
    print("Going", distance, "by", car)
    car.drive(distance)
    print("fuel left", car._Car__fuel)


if __name__ == '__main__':
    car = Car(1000)
    print("car:", car)
    # car._Car__fuel = 100
    # print("car fuel:", car.fuel)
    print("Drive, fuel left:", car.drive(15))
    print(car)
    print("Fuel left:", car.add_fuel(100))

    # car.drive(30)
    # car.drive(30)
    # car.drive(30)

    sport_car = SportCar(500)

    print("car sound:")
    car.make_sound()
    print("sport car sound:")
    sport_car.make_sound()

    sport_car.drive(10)
    sport_car._Car__fuel = 300
    sport_car.drive(10)

    car.add_fuel(300)
    drive_by_car(car, 70)
    sport_car.add_fuel(1000)
    drive_by_car(sport_car, 30)
