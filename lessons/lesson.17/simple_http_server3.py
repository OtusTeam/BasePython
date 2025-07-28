import socket
from pprint import pprint

HOST = '127.0.0.1'
PORT = 8081

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print('Waiting for connection...')
    print(f'Сервер запущен http://{HOST}:{PORT}')

    client_socket, client_address = server_socket.accept()
    with client_socket:
        print(f"Подключение от {client_address}")

        request = client_socket.recv(1024)
        request_text = request.decode('utf-8')
        print(f"Запрос от клиента:\n{request_text}")

        print("*" * 50)
        request_text = request_text.split("\r\n")

        print(request_text)
        print("*" * 50)
        request_line = request_text[0]
        print(f"Стартовая строка запроса: {request_line}")

        method, path, protocol = request_line.split()

        print(f"Метод запроса: {method}")
        print(f"Путь запроса: {path}")
        print(f"Протокол запроса: {protocol}")

        print("*" * 50)

        headers = {}
        for line in request_text[1:]:
            if line == "":
                break
            key, value = line.split(":", 1)
            headers[key.strip()] = value.strip()
        print("Заголовки запроса:")
        pprint(headers)


        print("*" * 50)
        print("*" * 50)

        if path == "/":
            response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html\n; charset=utf-8\r\n"
                "\n"
                "<h1>Hello, World!</h1>\r\n"
            )
        elif path.startswith("/home"):
            response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html\n; charset=utf-8\r\n"
                "\n"
                "<h1>Hello, Home!</h1>\r\n"
            )
        else:
            response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html\n; charset=utf-8\r\n"
                "\n"
                "<h1>ERROR!!!</h1>\r\n"
            )
        client_socket.sendall(response.encode('utf-8'))
        print("Ответ отправлен")
