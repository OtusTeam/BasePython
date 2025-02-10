from wsgiref.simple_server import make_server
from urllib.parse import parse_qs


def simple_app(environ, start_response):
    status = "200 OK"  # HTTP-статус ответа
    headers = [("Content-Type", "text/plain")]  # Заголовки
    start_response(status, headers)

    query_params = environ.get("QUERY_STRING")
    params = parse_qs(query_params)
    name = params.get("name")[0]
    return [f"Привет: {name}".encode("utf-8")]  # Ответ в виде списка байтов


server = make_server("localhost", 8000, simple_app)
print("Server running on http://localhost:8000")
server.serve_forever()