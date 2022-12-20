

class NoWeatherForCity(ValueError):
    pass


print(NoWeatherForCity.mro())

WEATHER_FORECAST = {
    "moscow": {
        "temp": 5,
        "rain_chance": 52,
    },
    "sochi": {
        "rain_chance": 20,
    },
}


def get_weather(city: str) -> dict:
    forecast = WEATHER_FORECAST.get(city)
    if not forecast:
        raise NoWeatherForCity(f"no data for city {city!r}")

    return forecast


def rain_tomorrow(city: str) -> bool | None:
    print("Will it rain in", city)
    try:
        weather = get_weather(city)
    except ValueError:
        print("could not get")
        return

    if "rain_chance" in weather:
        return weather["rain_chance"] > 50


print(rain_tomorrow("moscow"))
print(rain_tomorrow("voronezh"))
print(rain_tomorrow("sochi"))

