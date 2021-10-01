from datetime import date
from collections import namedtuple


Weather = namedtuple("Weather", "city, temp, humidity, wind, chance_of_rain, chance_of_snow")

User = namedtuple("User", "id, name, author")
Author = namedtuple("Author", "id, user")


def get_user(user_id: int):
    username = "john"
    email = "johnsmith@example.com"
    birth_date = date.today()
    return user_id, username, email, birth_date


def get_weather_old(city: str):
    temp = 21
    humidity = 40
    wind = 2
    chance_of_rain = 25
    chance_of_snow = 0
    # return city, temp, humidity, wind, chance_of_rain
    return {
        "city": city,
        "temp": temp,
        "humidity": humidity,
        "wind": wind,
        "chance_of_rain": chance_of_rain,
        "chance_of_snow": chance_of_snow,
    }


def get_weather(city: str):
    temp = 21
    humidity = 40
    wind = 2
    chance_of_rain = 25
    chance_of_snow = 0
    weather = Weather(city, temp, humidity, wind, chance_of_rain, chance_of_snow)
    return weather


def main():
    user = get_user(1)
    _, username, email, birth_date = user
    print(user)
    print(username)
    print(email)
    print(birth_date)

    weather = get_weather_old("Moscow")
    print(weather)
    chance_of_rain = weather["chance_of_rain"]
    print(chance_of_rain)

    chance_of_snow = weather["chance_of_snow"]
    print(chance_of_snow)

    weather = get_weather("Moscow")
    print(weather)
    print(weather.city)
    print(weather.chance_of_rain)
    city, temp, humidity, wind, chance_of_rain, chance_of_snow = weather
    print(city)
    print(temp)


def demo_relation():
    user = User(123, "Vasya", "author")
    print(user)
    author = Author(1, user)
    print(author)


if __name__ == '__main__':
    # demo_relation()
    main()
