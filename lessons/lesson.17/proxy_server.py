import socket
import threading


HOST = '127.0.0.1'
PORT = 8888


def handle_client(client_socket):
    request_bytes = client_socket.recv(4096)

    request_text = request_bytes.decode('utf-8', errors='ignore')
    print('Запрос от клиента получен')
    print(request_text)

    request_line = request_text.split('\r\n')[0]

    parts = request_line.split(' ')
    print(parts)
    if len(parts) < 3:
        print('Некорректный запрос')
        client_socket.close()
        return

    method = parts[0]
    url = parts[1]   # http://google.com/search

    if url.startswith('http://'):
        url = url[7:]                           # google.com/search/
    elif url.startswith('https://'):
        url = url[8:]
    else:
        print('Некорректный URL')
        client_socket.close()
        return

    if '/' in url:
        remote_host, remote_path = url.split('/', 1)    # google.com  и search
        remote_path = '/' + remote_path
    else:
        remote_host = url     # google.com
        remote_path = '/'     # /search


    print(f'Перенаправляем на хост {remote_host} и путь {remote_path}')

    try:
        remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        remote_socket.connect((remote_host, 80))

        request_text = request_text.replace(parts[1], remote_path, 1)

        remote_socket.sendall(request_text.encode('utf-8'))

        while True:
            data = remote_socket.recv(4096)
            if not data:
                break
            client_socket.sendall(data)
        remote_socket.close()

    except Exception as e:
        print(f'Ошибка при подключении {e}')

    client_socket.close()


def start_proxy():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))

    server_socket.listen(5)

    print('Прокси сервер запущен')

    while True:
        client_socket, addres =server_socket.accept()
        print(f'Новое подключение {addres}')
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()


if __name__ == '__main__':
    start_proxy()
