import requests
from pprint import pprint
from config import TOKEN_OWM


def get_weather(our_city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = TOKEN_OWM
    city = our_city

    params = {
        'q': our_city,
        'appid': api_key,
        'units': 'metric',
        'lang': 'ru',
    }

    response = requests.get(url, params=params)


    if response.status_code == 200:
        data = response.json().get('main').get('temp')
        return data


if __name__ == '__main__':
    weather = get_weather('Владивосток')
    print(weather)