import requests
import config
import pprint


def get_film(title, api_key):
    url = 'http://www.omdbapi.com/'
    params = {
        't': title,
        'apikey': api_key,
        'plot': 'full',
        'r': 'json'
    }
    try:
        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json().get('Plot')

    except requests.exceptions.Timeout:
        print("Превышено время ожидания запроса.")

    except requests.exceptions.ConnectionError:
        print("Произошла ошибка соединения с сервером.")

    except requests.exceptions.RequestException as e:
        print(f"Произошла ошибка при выполнении запроса: {e}")

    return None


if __name__ == '__main__':
    api_key = config.token_omdb
    title = 'Seven'

    result = get_film(title, api_key)
    print(result)