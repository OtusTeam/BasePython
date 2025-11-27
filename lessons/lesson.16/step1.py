# 1. http://google.com/search/?key=cat
# 2. Метод (GET, POST, PUT, DELETE)
# 3, Заголовки
# 4. Тело запроса

import requests
# from pprint import pprint


url = "https://google.com/"

response = requests.get(url)

print(type(response))
print(response.status_code)
if response:
    print(response.headers)
