import socket


HOST = '127.0.0.1'
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print('Waiting for connection...')
    print(f'Сервер запущен http://{HOST}:{PORT}')

    client_socket, client_address = server_socket.accept()
    with client_socket:
        print(f"Подключение от {client_address}")

        request = client_socket.recv(1024)
        print(f"Запрос от клиента:\n{request.decode('utf-8')}")

        response = (
            "HTTP/1.1 200 OK\n"
            "Content-Type: text/html\n; charset=utf-8\n"
            "\n"
            "<h1>Hello, World!</h1>\n"
        )
        client_socket.sendall(response.encode('utf-8'))
        print("Ответ отправлен")