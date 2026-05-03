import socket


HOST = '127.0.0.1'
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)
    print(f'Сервер запущен на http://{HOST}:{PORT}')

    client_socket, client_adress = server_socket.accept()
    print(f'Клинетский socket {client_socket=}, {client_adress=}')

    with client_socket:
        print(f'Подключение от  {client_adress=}')
        request = client_socket.recv(1024)
        print(f'Запрос от клиента:\n{request.decode()}')

        response = (
            "HTTP/1.1 200 OK\n"
            "Content-Type: text/html; charset=utf-8\n"
            "\r\n"
            "<h1>Hello world</h1>"
        )

        client_socket.sendall(response.encode())
        print(f'Запрос отправлен клиенту {client_adress}\n{response}')