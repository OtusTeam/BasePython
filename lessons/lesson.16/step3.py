# https://openweathermap.org/

import requests
from config import TOKEN_OPENWEATHER
from pprint import pprint


def get_weather(our_city):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    api_key = TOKEN_OPENWEATHER
    city = our_city

    params = {
        'appid': api_key,
        'q': city,
        'units': 'metric',
        'lang': 'ru',
    }

    response = requests.get(url, params=params)
    # print(response.url)
    # print(response.status_code)

    if response.status_code == 200:
        data = response.json()
        data = data.get('main').get('temp')
        # data = response.content
        # print(data)
    elif response.status_code == 404:
        data = f'Город {city} не найден'
    else:
        print(response.status_code)
        data = None
    return data


if __name__ == '__main__':
    print(11111)
    result = get_weather('Москва')
    pprint(result)