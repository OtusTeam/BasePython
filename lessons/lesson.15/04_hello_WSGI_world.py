def simple_app(environ, start_response):
    # Статус ответа
    status = '200 OK'
    # Заголовки ответа
    headers = [('Content-type', 'text/plain; charset=utf-8')]
    # Начало ответа
    start_response(status, headers)
    # Тело ответа
    return [b"Hello, WSGI World!"]

# Запуск сервера с помощью wsgiref
from wsgiref.simple_server import make_server

# Создание WSGI-сервера
httpd = make_server('localhost', 8051, simple_app)
print("Serving on port 8051...")

# Запуск сервера
httpd.serve_forever()

'''Далее преходите через браузер на адрес http://localhost:8051/'''
