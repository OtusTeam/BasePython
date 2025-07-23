import requests


# print(requests.__version__)
url =  'https://ya.ru/search'
params = {
    "text": "python",
    "lang": "ru"
}

response = requests.get(url, params=params)

# print(type(response))
print(response.status_code)

if response:
    print(response.text)
    print(response.headers)