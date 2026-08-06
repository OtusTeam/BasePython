import requests


# url = "https://httpbin.org/status/200"
# url = "https://httpbin.org/status/404"
# url = "https://httpbin.org/status/500"
url = "https://httpbin.org/redirect-to?url=https%3A%2F%2Fhttpbin.org%2Fget&status_code=302"

word = 'cat'
lang = 'ru'

params = {
    'text': word,
    'lang': lang
}

response = requests.get(url, params=params)

print(response)
print(type(response))
print(response.request.method)
print(response.request.url)

print(response.status_code)
print(response.reason)



