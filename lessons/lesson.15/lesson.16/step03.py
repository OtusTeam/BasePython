import requests


lang = 'ru'
prog = 'python'
url = "https://yandex.ru/search/"

params = {
    'text': prog,
    'lang': lang,
}

response = requests.get(url, params=params)


if response:
    print(response.content)
    print(response.headers)
    print(response.text)
else:
    print('NO')