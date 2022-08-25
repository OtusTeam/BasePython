

def get_weather_conditions(city: str):
    if city.lower() != "moscow":
        raise ValueError("invalid city")

    return {
        # "temp": 23,
        # "humidity": 50,
        "rain_chance": 60,
    }


def rain_tomorrow(city) -> bool | None:
    print("Will it rain tomorrow?")
    # return True
    # return False
    try:
        conditions = get_weather_conditions(city)
    except ValueError:
        return None
        # return

    if "rain_chance" not in conditions:
        return None

    return conditions["rain_chance"] > 50

    # if (rain_chance := conditions.get("rain_chance")) is None:
    #     return None
    # return rain_chance > 50


res = rain_tomorrow("Omsk")
# res = get_weather_conditions("Omsk")
print("res for Omsk:", res)

res = rain_tomorrow("Sochi")
print("res for Sochi:", res)

res = rain_tomorrow("Moscow")
print("res for Moscow:", res)
