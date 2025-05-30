# https://google.com/api/v1/data/weather?q=Moscow&id=key

import requests

#print(requests.__version__)

url = 'https://example.com'
# url = 'https://pikabu.ru'

response = requests.get(url)

print(response)

if response.status_code == 200:
    print('OK')
    print(response.headers)
    print(response.text)