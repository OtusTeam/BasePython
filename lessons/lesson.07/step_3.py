# a = 1
# b = "2"
#
# c = a + b
# print(c)
#
# d = c ** 2
#
# print(d)


def get_weather_conditions(city):
    if city != "Moscow":
        raise ValueError("invalid city")
    return {
        "temp": 13,
        "humidity": 50,
        "rain_chance": 0,
    }


def rain_tomorrow(city):
    print("Will it rain in", city)
    # return True
    # return False
    try:
        weather = get_weather_conditions(city)
    except ValueError:
        return None

    return weather["rain_chance"] > 50


res = rain_tomorrow("Perm")
print("res:", res)
print("Hello!")


res = rain_tomorrow("Moscow")
print("res:", res)
