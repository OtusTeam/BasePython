import requests


url = 'http://127.0.0.1:8080/about'

data = {
    'name': 'Bob',
    'age': 32,
    'email': 'bob@mail.ru'
}

# response = requests.post(url, data=data)
response = requests.get(url)
print(response.status_code)
print(response.text)