import requests


# url = 'https://yandex.ru/search/?text=dog&lang=ru'

word = 'cat'
lang = 'ru'

url = f'https://yandex.ru/search/?text={word}&lang={lang}'

response = requests.get(url)
print(f'Код статутса: {response.status_code}')
if response:
    # print(response.headers)
    print(response.text)
else:
    print('NO')
