import requests
from functools import partial
from termcolor import colored

# Функция для цветного вывода
def print_color(message, color):
    print(colored(message, color))

# Создание новых функций для цветного вывода
print_green = partial(print_color, color='green')
print_red = partial(print_color, color='red')

# GET-запрос (пример успешного запроса)
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
if response.status_code == 200:
    print_green('GET request successful!')
    print_green('Response JSON:')
    print(response.json())
else:
    print_red(f'GET request failed with status code: {response.status_code}')

# GET-запрос (пример неудачного запроса)
response = requests.get('https://jsonplaceholder.typicode.com/posts/1000')  # нет такого ID
if response.status_code == 200:
    print_green('GET request successful!')
    print_green('Response JSON:')
    print(response.json())
else:
    print_red(f'GET request failed with status code: {response.status_code}')

# POST-запрос (пример успешного запроса)
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
if response.status_code == 201:
    print_green('POST request successful!')
    print_green('Response JSON:')
    print(response.json())
else:
    print_red(f'POST request failed with status code: {response.status_code}')

# PUT-запрос (пример успешного запроса)
data = {
    'id': 1,
    'title': 'foo updated',
    'body': 'bar updated',
    'userId': 1
}
response = requests.put('https://jsonplaceholder.typicode.com/posts/1', json=data)
if response.status_code == 200:
    print_green('PUT request successful!')
    print_green('Response JSON:')
    print(response.json())
else:
    print_red(f'PUT request failed with status code: {response.status_code}')

# DELETE-запрос (пример успешного запроса)
response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
if response.status_code == 200:
    print_green('DELETE request successful!')
else:
    print_red(f'DELETE request failed with status code: {response.status_code}')
