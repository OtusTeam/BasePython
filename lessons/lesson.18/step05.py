import requests


url = "https://api.openweathermap.org/data/2.5/weather"

word = 'cat'
lang = 'ru'

params = {
    'text': word,
    'lang': lang
}

data1 = {
    'user_name': 'Bob',
    'user_age': 31,
    'user_password': '123qaz',
}

headers = {
    'User-Agent': 'MyOtus',
    'Token_OTUS': "12345qwerty",
}

response = requests.post(url, params=params, headers=headers, data=data1)
# response = requests.delete(url)
# response = requests.post(url, params=params, headers=headers, json=json1)


if response.status_code == 200:
    print(response)
    print(type(response))
    print(response.request.method)
    print(response.request.url)
    print(response.request.headers)
    # print(response.request.body)
    print(response.text)
    print(response.status_code)

    data = response.json()
    print(data)
    print(type(data))

