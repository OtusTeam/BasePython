import requests


url = "https://httpbin.org/headers"

headers = {
    'User-Agent': "MyOtus",
    'Token_OTUS': '1234567qwerty'
}

response = requests.get(url, headers=headers)


if response:
    print(response.headers)
    print(response.text)
else:
    print('NO')