import requests
from pprint import pprint


# url = 'https://ya.ru/search/'
url = 'https://nalog.ru'

params = {
    'text': 'python',
    'lang': 'ru',
}

# response = requests.get(url, params=params)
response = requests.get(url)
print(response.status_code)

if response.status_code == 200:
    # print(response.text)
    pprint(response.headers)