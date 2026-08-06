import requests

from config import TOKEN_OWM


def get_weather(our_city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = TOKEN_OWM
    lang = 'ru'
    city = our_city

    params = {
        'q': city,
        'lang': lang,
        'appid': api_key,
        'units': 'metric',
    }

    response = requests.get(url, params=params)

    print(response.status_code)
    if response.status_code == 200:
        data = response.json().get('main').get('temp')
        return data
    else:
        return None


if __name__ == '__main__':
    weather = get_weather('Махачкала')
    print(weather)