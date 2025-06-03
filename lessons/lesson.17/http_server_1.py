import socket


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

        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html\r\n; charset=utf-8\r\n"
            "\r\n"
            "<h1>Hello World!</h1>"
        )
        client_socket.sendall(response.encode())
        print("Ответ отправлен клиенту")

