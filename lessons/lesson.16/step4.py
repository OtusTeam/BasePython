import requests


url = 'https://yandex.ru/search/'

params = {
    'text': 'python',
    'lang': 'ru',
}
response = requests.get(url, params=params)
response = requests.post(url, params=params)
response = requests.put(url, params=params)
response = requests.delete(url, params=params)

print(response)

if response.status_code == 200:
    print('OK')
    print(response.headers)
    print(response.text)