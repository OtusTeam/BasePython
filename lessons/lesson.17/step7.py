from wsgiref.simple_server import make_server


def simple_app(environ, start_response):
    status = "200 OK"  # HTTP-статус ответа
    headers = [("Content-Type", "text/plain")]  # Заголовки
    start_response(status, headers)

    method = environ.get("REQUEST_METHOD")
    if method == "POST":
        print('123')
    path = environ.get("PATH_INFO")
    return [f"Метод: {method}, Путь: {path}".encode("utf-8")]  # Ответ в виде списка байтов


server = make_server("localhost", 8000, simple_app)
print("Server running on http://localhost:8000")
server.serve_forever()