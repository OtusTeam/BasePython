import socket
from pprint import pprint


HOST = '127.0.0.1'
PORT = 8081

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)
    print(f'Сервер запущен на http://{HOST}:{PORT}')

    client_socket, client_adress = server_socket.accept()
    print(f'Клинетский socket {client_socket=}, {client_adress=}')

    with client_socket:
        print(f'Подключение от  {client_adress=}')
        request = client_socket.recv(1024)
        request_text = request.decode('utf-8')
        print(f'Запрос от клиента:\n{request_text}')
        print('*' * 50)
        request_lines = request_text.split('\r\n')
        print(f'{request_lines=}')
        request_line = request_lines[0]
        print(f'Стартовая строка запроса:\n{request_line}')
        print('*' * 50)
        method, path, protocol = request_line.split()
        print(f'Метод запроса: {method}')
        print(f'Путь запроса: {path}')
        print(f'Версия протокола: {protocol}')

        headers = {}

        for line in request_lines[1:]:
            if line == "":
                break
            key, value = line.split(':', 1)
            headers[key.strip()] = value.strip()
        print('Заголовки запроса:')
        pprint(headers)

        response = (
            "HTTP/1.1 200 OK\n"
            "Content-Type: text/html; charset=utf-8\n"
            "\r\n"
            "<h1>Hello world</h1>"
        )
        print('*' * 50)
        print('*' * 50)
        client_socket.sendall(response.encode())
        print(f'Запрос отправлен клиенту {client_adress}\n{response}')