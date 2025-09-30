import requests


url = 'http://127.0.0.1:8081/home'
data = {
    'name': 'Ivan',
    'age': 22,
    'email': 'ivan@mail.ru',
    'password': '123',
    'message': 'Hello, Ivan'
}

response = requests.post(url, data=data)
print(response.status_code)
print(response.text)