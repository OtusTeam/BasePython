import requests


url = 'http://127.0.0.1:8080/about'

data = {
    'name': 'Bob',
    'age': 21,
    'email': 'bob@mail.ru'
}

# response = requests.get(url)
response = requests.post(url, data=data)
print(response.status_code)
print(response.text)