import requests
import config
import pprint


def get_weather(city, api_key):
    url = f'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',
        'lang': 'ru'
    }
    try:
        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json().get('main').get('temp')

    except requests.exceptions.Timeout:
        print("Превышено время ожидания запроса.")

    except requests.exceptions.ConnectionError:
        print("Произошла ошибка соединения с сервером.")

    except requests.exceptions.RequestException as e:
        print(f"Произошла ошибка при выполнении запроса: {e}")

    return None

if __name__ == '__main__':
    api_key = config.token_weather
    city = 'Севастополь'

    result = get_weather(city, api_key)
    pprint.pprint(result)
