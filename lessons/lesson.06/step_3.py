from random import random


class BaseWeatherException(Exception):
    pass


class WeatherApiConnectionError(BaseWeatherException):
    pass


class CityNotFoundError(BaseWeatherException):
    def __init__(self, city, message):
        self.city = city
        super().__init__(message)


WEATHER_FORECAST = {
    "moscow": {
        "temp": 10,
        "humidity": 60,
        "rain_chance": 70,
    },
    "sochi": {
        "temp": 20,
        "humidity": 50,
        "rain_chance": 20,
    },
}


def get_weather_conditions(city: str) -> dict:
    if random() > 0.8:
        raise WeatherApiConnectionError("could not connect")

    weather = WEATHER_FORECAST.get(city.lower())
    if weather:
        return weather

    msg = f"no data for city {city}"
    raise CityNotFoundError(city, msg)


def rain_tomorrow(city: str) -> bool | None:
    try:
        weather = get_weather_conditions(city)
    except CityNotFoundError as exc:
        print("city:", exc.city, "error:", exc)
        return
    except BaseWeatherException as exc:
        print("some other weather exception:", exc)
        return

    # weather = get_weather_conditions(city)
    return weather["rain_chance"] > 50


def bulk_rain_check(*cities: str):
    for city in cities:
        print("rain tomorrow in city", city)
        rain_tomorrow(city)


print("rain in Moscow?", rain_tomorrow("Moscow"))
print("rain in Voronezh?", rain_tomorrow("Voronezh"))
print("rain in Sochi?", rain_tomorrow("Sochi"))

# try:
#     bulk_rain_check("Moscow", "Voronezh", "Sochi")
# except CityNotFoundError as exc:
#     print("error bulk check, stopped on", exc.city)
