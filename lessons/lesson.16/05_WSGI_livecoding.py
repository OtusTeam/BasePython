import os
from functools import partial
from termcolor import colored
import csv
import json

os.system('clear')

# Функция для цветного вывода
def print_color(message, color):
    print(colored(message, color))

# Создание новых функций для цветного вывода
print_green = partial(print_color, color='green')

'''
Обязательно протестируйте каждый путь через Postman!
'''

# Создаем CSV-файл и записываем заголовки, если файл не существует
csv_file_path = 'data.csv'
if not os.path.exists(csv_file_path):
    with open(csv_file_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Name', 'City', 'Age'])

def simple_app(environ: dict, start_response):
    """Простое WSGI-приложение для обработки различных HTTP-запросов.

        Обрабатывает следующие пути:
        - '/' (GET): Возвращает приветственное сообщение.
        - '/goodbye' (GET): Возвращает прощальное сообщение.
        - '/info' (GET): Возвращает метод запроса.
        - '/get_people' (GET): Возвращает содержимое файла data.csv в формате JSON.
        - '/add_person' (POST): Добавляет новую запись в CSV-файл с данными из тела запроса в формате JSON.
        - Все другие пути: Возвращает ошибку 404 (Not Found).

        @param environ: Словарь с информацией о запросе (заголовки, параметры запроса и т.д.).
        @param start_response: Функция, которая должна быть вызвана для отправки ответа (статус и заголовки).
        @return: Итератор байтов, содержащий тело ответа.
    """
    # Получение метода запроса
    request_method = environ.get('REQUEST_METHOD', 'GET')
    # Получение пути запроса
    path = environ.get('PATH_INFO', '/')
    # Получение строки запроса
    
    # Обработка пути запроса
    if path == '/':
        # Корневой путь, возвращаем приветственное сообщение
        response_body = b"Hello, WSGI World!"
        status = '200 OK'
        
    elif path == '/goodbye':
        # Путь для прощания, возвращаем сообщение прощания
        response_body = b"Goodbye, WSGI World!"
        status = '200 OK'

    elif path == '/info':
        # Путь для получения информации о запросе
        response_body = f"Request Method: {request_method}".encode('utf-8')
        status = '200 OK'

    elif path == '/get_people' and request_method == 'GET':
        # Путь для получения содержимого data.csv в формате JSON
        people = []
        with open(csv_file_path, 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                people.append(row)
        response_body = json.dumps(people).encode('utf-8')
        status = '200 OK'

    elif path == '/add_person' and request_method == 'POST':
        # Путь для добавления новой записи в CSV-файл через POST-запрос
        try:
            request_body_size = int(environ.get('CONTENT_LENGTH', 0))
        except (ValueError):
            request_body_size = 0
        
        request_body = environ['wsgi.input'].read(request_body_size)
        try:
            data = json.loads(request_body.decode('utf-8'))
            name = data['Name']
            city = data['City']
            age = data['Age']
            with open(csv_file_path, 'a', newline='') as csvfile:
                csvwriter = csv.DictWriter(csvfile, fieldnames=['Name', 'City', 'Age'])
                csvwriter.writerow({'Name': name, 'City': city, 'Age': age})
            response_body = b"Person added successfully!"
            status = '200 OK'
        except (json.JSONDecodeError, KeyError):
            response_body = b"Invalid data format. Expected JSON with 'Name', 'City', and 'Age'."
            status = '400 Bad Request'
    else:
        # Обработка неизвестного пути, возвращаем ошибку 404
        response_body = b"Not Found"
        status = '404 Not Found'
    
    # Заголовки ответа
    headers = [('Content-type', 'text/plain; charset=utf-8')]
    # Начало ответа
    start_response(status, headers)
    # Тело ответа
    return [response_body]

# Запуск сервера с помощью wsgiref
from wsgiref.simple_server import make_server

# Создание WSGI-сервера
httpd = make_server('localhost', 8051, simple_app)
print_green("Serving on port 8051...")

# Запуск сервера
httpd.serve_forever()
