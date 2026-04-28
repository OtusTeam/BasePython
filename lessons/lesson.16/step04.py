import requests


url = "https://httpbin.org/get"

word = 'cat'
lang = 'ru'

params = {
    'text': word,
    'lang': lang,
}

response = requests.get(url, params=params)
print(f'Код статутса: {response.status_code}')
if response:
    print(response.headers)
    print(response.text)
else:
    print('NO')



