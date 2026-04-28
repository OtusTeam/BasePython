import requests


url = "https://httpbin.org/post"
word = 'cat'
lang = 'ru'
params = {
    'text': word,
    'lang': lang,
}

headers = {
    'User-Agent': 'MyOtus',
    'Token_OTUS': '123456qwerty',
}

data = {
    'user_name': 'Bob',
    'user_pass': '123qwe',
    'user_age': '123qwe',
}

response = requests.post(url, params=params, headers=headers, data=data)
# response = requests.post(url, params=params, headers=headers, json=json)
print(f'Код статутса: {response.status_code}')
if response:
    print(response.headers)
    print(response.text)
else:
    print('NO')



