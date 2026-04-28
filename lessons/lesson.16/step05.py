import requests


url = "https://httpbin.org/headers"

headers = {
    'User-Agent': 'MyOtus',
    'Token_OTUS': '123456qwerty',
}

response = requests.get(url, headers=headers)
print(f'Код статутса: {response.status_code}')
if response:
    print(response.headers)
    print(response.text)
else:
    print('NO')



