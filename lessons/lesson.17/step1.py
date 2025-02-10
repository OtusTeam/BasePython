import requests

url = 'https://mail.ru'

response = requests.get(url)

print(response.status_code)
print(type(response))

print(response.text)