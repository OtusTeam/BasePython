import requests


word = 'cat'
lang = 'ru'

url = 'https://yandex.ru/search/'

params = {
    'text': word,
    'lang': lang,
}

response = requests.get(url, params=params)
print(f'Код статутса: {response.status_code}')
if response:
    # print(response.headers)
    print(response.text)
else:
    print('NO')
