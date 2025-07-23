# https://openweathermap.org/
import requests
from config import TOKEN_OPENWEATHER


def get_weather(city):

    url = "https://api.openweathermap.org/data/2.5/weather"

    api_keys = TOKEN_OPENWEATHER
    # city = "Сочи"

    params = {
        "q": city,
        "appid": api_keys,
        "units": "metric",
        "lang": "ru",
    }

    response = requests.get(url, params=params)
    # print(response.url)
    # print(response.status_code)

    if response.status_code == 200:
        data = response.json()
        # print()
        # print(type(data))
        data =  data.get("main").get("temp")
    elif response.status_code == 404:
        data = f'Город {city} не найден'
    else:
        print(response.status_code)
        data = None

    return data

if __name__ == '__main__':
    print(get_weather('Краснодар123'))