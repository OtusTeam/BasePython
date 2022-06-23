class BaseVehicle:
    def get_passengers_count(self):
        return 0


class Car(BaseVehicle):
    def __init__(self):
        self._passengers = 0

    def add_passenger(self):
        self._passengers += 1

    def remove_passenger(self):
        self._passengers -= 1

    def get_passengers_count(self):
        return self._passengers


class SportCar(Car):

    def get_passengers_count(self):
        count = super().get_passengers_count()
        old = BaseVehicle.get_passengers_count(self)
        print('old', old)
        print("got count", count)
        count -= 1
        return count


car = Car()
car.add_passenger()
car.add_passenger()
car.add_passenger()
print(car.get_passengers_count())


sport_car = SportCar()
sport_car.add_passenger()
sport_car.add_passenger()
print(sport_car.get_passengers_count())
