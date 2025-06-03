import socket
from pprint import pprint


HOST = '127.0.0.1'
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Сервер запущен на http://{HOST}:{PORT}")

    client_socket, client_address = server_socket.accept()
    with client_socket:
        print(f"Подключение от {client_address}")

        request = client_socket.recv(1024)
        print("Запрос от клиента: \n", request.decode())

        print("*" * 50)
        request_text = request.decode('utf-8')
        request_lines = request_text.split("\r\n")

        print("*" * 50)
        print(f"Вся строка")
        pprint(request_lines)

        request_line = request_lines[0]

        print("*" * 50)
        print(f"Стартовая строка: {request_line}")

        method, path, protocol = request_line.split()
        print("*" * 50)
        print(f"Метод запроса: {method}")
        print(f"Путь запроса: {path}")
        print(f"Версия протоклоа: {protocol}")

        headers = {}

        for line in request_lines[1:]:
            if line == "":
                break
            key, value = line.split(":", 1)
            headers[key.strip()] = value.strip()

        print("*" * 50)
        print("Заголовки запроса: ")
        pprint(headers)

        if path == "/":
            response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html\r\n; charset=utf-8\r\n"
                "\r\n"
                
                "<h1>Hello World!</h1>"
            )

        elif path.startswith("/home"):
            response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html\r\n; charset=utf-8\r\n"
                "\r\n"
                "<h1>Hello Home!</h1>"
            )

        else:
            response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html\r\n; charset=utf-8\r\n"
                "\r\n"
                "<html lang='ru'> <h1>Error not found</h1> </html"
            )

        client_socket.sendall(response.encode())
        print("Ответ отправлен клиенту")

