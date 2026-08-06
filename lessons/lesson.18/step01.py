import requests


# url = "https://otus.ru/"
# url = "https://httpbin.org/get"

# url = "https://ya.ru/search/?text=dog&lang=ru"
word = 'cat'
lang = 'ru'
# url = f"https://ya.ru/search/?text={word}&lang={lang}"
url = f"https://ya.ru/search/"

params = {
    'text': word,
    'lang': lang
}

response = requests.get(url, params=params)

# if response.status_code == 200:
if response:
    print(response)
    print(type(response))
    print(response.request.method)
    print(response.request.url)
    print(response.request.headers)
    print(response.request.body)
    print(response.text)
