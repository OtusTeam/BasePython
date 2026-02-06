import requests


lang = 'ru'
prog = 'python rus'
url = f"https://yandex.ru/search/?text={prog}&lang={lang}"
# url = "https://yandex.ru/search/?text=python&lang=ru"
response = requests.get(url)


if response:
    print(response.content)
    print(response.headers)
    print(response.text)
else:
    print('NO')