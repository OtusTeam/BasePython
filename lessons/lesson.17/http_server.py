import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 8080))

server_socket.listen(1)
print("Север  запущен на  127.0.0.1 порту 8080")

running = True
while running:
    client_socket, client_address = server_socket.accept()
    print(f'Подкючен клиент  {client_address}')

    request_data = client_socket.recv(1024).decode('utf-8')
    print('Запрос получен')
    print(f'{request_data}')

    if 'POST' in request_data:
        body = request_data.split('\r\n\r\n')[1]
        print('Тело запроса')
        print(body)
        # running = False
        response = """\
        HTTP/1.1 200 OK
        Content-Type: text/html

        <html>
            <body>
                <h1>Привет, ПОСТ запрос!</h1>
            </body>
        </html>
        """

    else:
        response = """\
    HTTP/1.1 200 OK
    Content-Type: text/html
    
    <html>
        <body>
            <h1>Привет, мир!</h1>
        </body>
    </html>
    """

    client_socket.sendall(response.encode('utf-8'))
    client_socket.close()