# https://yandex.ru
# get post put delete
# headers
# body

import requests


# print(requests.__version__)

url = 'https://nalog.ru'
# url = 'https://nalog.ru/123'

response = requests.get(url)

print(f'Код статутса: {response.status_code}')
print(f'Объект response: {response}')
print(f'Тип response: {type(response)}')

# print(response.text)

# if response.status_code == 200:
if response:
    # print(response.headers)
    print(response.text)
else:
    print('NO')
