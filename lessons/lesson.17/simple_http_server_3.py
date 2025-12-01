import socket
from pprint import pprint


HOST = "127.0.0.1"
PORT = 8083

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(3)
    print(f"Сервер запущен на http://{HOST}:{PORT}")

    # while True:
        

    client_socket, client_address = server_socket.accept()

    with client_socket:
        print(f'Подключение от {client_address}')
        print('*' * 50)
        request = client_socket.recv(1024)
        request_text = request.decode('utf-8')
        print(f'Запрос от клиента {client_address}')
        print(f'{request_text}')
        print('*' * 50)

        request_lines = request_text.split('\r\n')

        request_line = request_lines[0]
        print(f'Первая строка {request_line}')

        method, path, protocol = request_line.split()
        print(f'Метод запроса: {method}')
        print(f'Путь запроса: {path}')
        print(f'Версия протокола {protocol}')
        print('*' * 50)
        print('*' * 50)

        headers = {}
        for line in request_lines[1:]:
            if line == '':
                break
            key, value = line.split(':', 1)
            headers[key.strip()] = value.strip()
        print('Заголовки запроса:')
        pprint(headers)
        print('*' * 50)
        print('*' * 50)

        if path == '/':
            response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html; charset=utf-8\r\n"
                "\r\n"
                "<h1>Hello World!!!</h1>"
            )

        elif path.startswith('/about_us') and method == 'GET':
            response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html; charset=utf-8\r\n"
                "\r\n"
                "<h2>GET - О нас!</h2>"
            )
        elif path.startswith('/about_us') and method == 'POST':
            response = (
                "HTTP/1.1 201 OK\r\n"
                "Content-Type: text/html; charset=utf-8\r\n"
                "\r\n"
                "<h2>POST - О нас!</h2>"
            )
        client_socket.sendall(response.encode())
        print(f'Запрос отправлен клиенту {client_address} - {response}')