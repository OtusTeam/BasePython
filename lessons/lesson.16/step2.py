# 1. http://google.com/search/?key=cat
# 2. Метод (GET, POST, PUT, DELETE)
# 3, Заголовки
# 4. Тело запроса

import requests
# from pprint import pprint

# 1
url1 = "https://ya.ru/search?query=python&lang=ru"
response_1 = requests.get(url1)

# 2
lang = 'ru'
query = 'python'
url2 = f"https://ya.ru/search?query={query}&lang={lang}"
response_2 = requests.get(url2)

# 3
url3 = "https://ya.ru/search"
params = {
    "lang": 'ru',
    "text": 'python',
}
response = requests.get(url3, params=params)

print(response.status_code)
if response:
    print(response.headers)
    print(response.text)

