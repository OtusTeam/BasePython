class InvalidCity(Exception):
    def __init__(self, message):
        self.city = message
        super().__init__(message)


print(InvalidCity.mro())

WEATHER_FORECAST = {
    "moscow": {
        "rain_chance": 52,
        "humidity": 60,
    },
    "omsk": {
        "temp": 15,
        "rain_chance": 42,
    },
}

missing = object()


def get_weather(city):
    forecast = WEATHER_FORECAST.get(city.lower(), missing)
    if forecast is missing:
        raise InvalidCity(city)

    return forecast


def rain_tomorrow(city):
    """
    :param city:
    :return: bool (True or False) or None
    """
    # weather = get_weather(city)
    try:
        weather = get_weather(city)
    except InvalidCity as e:
        print("could not find weather for", e.args, e.city)
        return
    print("weather conditions for", city, "-", weather)

    return weather["rain_chance"] > 50


print(rain_tomorrow("Moscow"))
print(rain_tomorrow("Omsk"))
print(rain_tomorrow("Voronezh"))
print(rain_tomorrow("Sochi"))

try:
    print(rain_tomorrow("Sochi"))
except InvalidCity as e:
    print("e", e)
print(rain_tomorrow("Moscow"))
