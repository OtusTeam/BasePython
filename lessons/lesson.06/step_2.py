
WEATHER_FORECAST = {
    "moscow": {
        "temp": 13,
        "humidity": 40,
        "rain_chance": 52,
    },
    # "Moscow": {},
    # "sochi": None,
    "voronezh": {
        "rain_chance": 50,
    }
}


missing = object()


def get_weather_conditions(city: str):
    # if (forecast := WEATHER_FORECAST.get(city.lower())) is not None:
    # if city in WEATHER_FORECAST:
    #     return WEATHER_FORECAST[city]
    # forecast = WEATHER_FORECAST.get(city, "missing")
    # if forecast == "missing": ...
    forecast = WEATHER_FORECAST.get(city.lower(), missing)
    if forecast is missing:
        raise ValueError(f"invalid city {city!r}")
        # return None
        # try:
        #     raise ValueError(f"invalid city {city!r}")
        # except ValueError:
        #     return None
    return forecast


# from typing import Optional, Union
# Optional[bool]
# Union[bool, None]


# isinstance(value, (int, float))
# def rain_tomorrow(city: str) -> bool:
# def rain_tomorrow(city: str) -> Optional[bool]:
def rain_tomorrow(city: str) -> bool | None:
    print("Will it rain in", city)
    try:
        weather = get_weather_conditions(city)
    # except (ValueError, TypeError):
    except ValueError:
        # raise CityError()
        # return None
        return

    # return weather["rain_chance"]

    return weather["rain_chance"] > 50


print(get_weather_conditions("Moscow"))
# print(get_weather_conditions("Sochi"))
# print(get_weather_conditions("Voronezh"))


print(rain_tomorrow("Moscow"))
print(rain_tomorrow("Sochi"))
print(rain_tomorrow("Voronezh"))
