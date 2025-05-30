import requests


url = 'https://yandex.ru/search/'

headers = {
    'User-Agent': "MyTest"
}

response = requests.get(url, headers=headers)

print(response)

if response.status_code == 200:
    print('OK')
    print(response.headers)
    print(response.text)