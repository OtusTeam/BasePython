import socket
from pprint import pprint


HOST = '127.0.0.1'
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f'Сервер запущен на http://{HOST}:{PORT}')

    client_socket, client_address = server_socket.accept()
    # c = server_socket.accept()
    # client_socket = c[0]
    # client_address = c[1]

    with client_socket:
        print(f'Подключение от {client_address}')

        request = client_socket.recv(1024)
        request_text = request.decode('utf-8')
        print('Запрос от клиента:\n ', request_text)

        print('*' * 50)
        request_text = request_text.split('\r\n')
        print(request_text)

        print('*' * 50)
        request_line = request_text[0]
        print(f'Стартовая строка запроса: {request_line}')
        print('*' * 50)

        method, path, protocol = request_line.split()
        print(f'Метод запроса: {method}')
        print(f'Путь запроса:  {path}')
        print(f'Версия протокола: {protocol}')

        print('*' * 50)

        headers = {}
        for line in request_text[1:]:
            if line == '':
                break
            # print(line)
            # print(line.split(':'))
            key, value = line.split(':', 1)
            headers[key.strip()] = value.strip()
        print('Заголовки запроса:')
        pprint(headers)

        print('*' * 50)


        print('*' * 50)

        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html\r\n"
            "\r\n"
            "<h3>Hello world!!!</h1>"
        )
        client_socket.sendall(response.encode('utf-8'))
        print('Ответ отправлен пользователю')