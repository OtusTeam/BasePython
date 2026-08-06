import requests


url = "https://httpbin.org/get"

word = 'cat'
lang = 'ru'

params = {
    'text': word,
    'lang': lang
}

response = requests.get(url, params=params)

if response.status_code == 200:
    print(response)
    print(type(response))
    # print(response.request.method)
    print(response.request.url)
    # print(response.request.headers)
    # print(response.request.body)
    # print(response.text)
    # print(response.content)

    data = response.json()
    print(data)
    print(type(data))

