import requests
import config
import pprint


def get_weather(city, api_key):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('main').get('temp')
    else:
        return None

if __name__ == '__main__':
    api_key = config.token_weather
    city = 'Сочи'

    result = get_weather(city, api_key)
    pprint.pprint(result)


