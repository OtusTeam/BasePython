import requests
from pprint import pprint
from config import TOKEN_OPENWEATHER


def get_weather(our_city):
    url = 'https://api.openweathermap.org/data/2.5/weather123'
    api_key = TOKEN_OPENWEATHER
    city = our_city

    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',
        'lang': 'ru',
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        data = data.get('main').get('temp')
    elif response.status_code == 404:
        data = f'Город {city=} не найден'

    return data


if __name__ == '__main__':
    weather = get_weather("Сочи")
    print(weather)