class BaseWeatherException(Exception):
    pass


class CityNotFoundError(BaseWeatherException):
    def __init__(self, city, message):
        super().__init__(message)
        self.city = city


WEATHER_FORECAST = {
    "moscow": {
        "temp": 20,
        "humidity": 40,
        "rain_chance": 70,
    },
    "sochi": {
        "temp": 25,
        "humidity": 50,
        "rain_chance": 20,
    },
}


def get_weather_conditions(city: str) -> dict:
    # weather = WEATHER_FORECAST.get(city.lower())
    # if weather:
    #     return weather
    if weather := WEATHER_FORECAST.get(city.lower()):
        return weather

    message = f"no weather for city {city}"
    raise CityNotFoundError(city, message)


def rain_tomorrow(city: str) -> bool | None:
    try:
        weather = get_weather_conditions(city=city)
    except CityNotFoundError:
        return

    # weather = get_weather_conditions(city=city)
    return weather["rain_chance"] >= 50


def print_weathers(cities: list[str]):
    for city in cities:
        print("rain in", city)
        try:
            print(rain_tomorrow(city))
        except CityNotFoundError:
            print("city not found", city)


def rains_dict(cities: list[str]):
    try:
        return {
            city: rain_tomorrow(city)
            for city in cities
        }
    except CityNotFoundError as ex:
        print("error on city", ex.city)

#
# print("rain in Moscow", rain_tomorrow("Moscow"))
# print("rain in Voronezh", rain_tomorrow("Voronezh"))
# print("rain in Sochi", rain_tomorrow("Sochi"))


print()
print_weathers(["Voronezh", "Sochi"])

res = rains_dict(["Voronezh", "Sochi"])
print(res)
