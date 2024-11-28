import os
import csv
import json
from wsgiref.simple_server import make_server
import logging

# Настройка логгера
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger()

# Создаем CSV-файл и записываем заголовки, если файл не существует
csv_file_path = 'data.csv'
if not os.path.exists(csv_file_path):
    with open(csv_file_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['name', 'city', 'age'])

def simple_app(environ, start_response):
    """Простое WSGI-приложение для обработки HTTP-запросов.

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
    request_method = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']

    if path == '/':
        # print(environ)
        response_body = b"Hello, WSGI World!\n"
        status = '200 OK'

    elif path == '/get_people' and request_method == 'GET':
        with open(csv_file_path, 'r') as csvfile:
            people = list(csv.DictReader(csvfile))
        # Сериализуем Python-объект (список словарей) в строку формата JSON
        response_body_json = json.dumps(people)

        # Кодируем JSON-строку в байты с использованием кодировки UTF-8
        response_body = response_body_json.encode('utf-8')

        status = '200 OK'

    elif path == '/add_person' and request_method == 'POST':
        # Получаем длину тела запроса в байтах из заголовка CONTENT_LENGTH
        content_length = int(environ['CONTENT_LENGTH'])
        print(f'{content_length=}')

        # Читаем указанное количество байтов из потока wsgi.input
        request_body = environ['wsgi.input'].read(content_length)
        print(f'{request_body=}, {type(request_body)=}')
        

        decoded_request_body = request_body.decode('utf-8')
        print(f'{decoded_request_body=}, {type(decoded_request_body)=}')

        data = json.loads(decoded_request_body)
        print(f'{data=}, {type(data)=}')

        with open(csv_file_path, 'a', newline='') as csvfile:
            csvwriter = csv.DictWriter(csvfile, fieldnames=['name', 'city', 'age'])
            csvwriter.writerow(data)
        response_body = b"Person added successfully!"
        status = '200 OK'

    else:
        response_body = b"Not Found"
        status = '404 Not Found'

    headers = [('Content-type', 'text/plain; charset=utf-8'), ('Custom-Header', 'foo-bar')]
    start_response(status, headers)
    return [response_body]

# Запуск сервера
httpd = make_server('localhost', 9999, simple_app)
logger.info(f"Serving on  http://localhost:9999...")
httpd.serve_forever()
