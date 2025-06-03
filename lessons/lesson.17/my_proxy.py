import socket
import threading
from pprint import pprint


HOST = '127.0.0.1'
PORT = 8080

LOG_FILE = "my_proxy.log"


def log_request(data):
    with open(LOG_FILE, 'a', encoding="utf-8") as log:
        log.write(f'{data} \n\n')


def handle_client(client_socket):
    request = client_socket.recv(4096)
    request_text = request.decode('utf-8')
    print("*" * 30)
    print("Запрос клиента: ")
    print(request_text)

    log_request(request_text)

    request_lines = request_text.split("\r\n")

    pprint(request_lines)
    request_line = request_lines[0]
    method, path, protocol = request_line.split()

    headers = {}

    for line in request_lines[1:]:
        if line == "":
            break
        key, value = line.split(":", 1)
        headers[key.strip()] = value.strip()

    my_adress = headers['Host']
    my_host, my_port = my_adress.split(':')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        try:
            server_socket.connect((my_host, my_port))
            server_socket.sendall(request)

            while True:
                data = server_socket.recv(4096)
                if not data:
                    break
                client_socket.sendall(data)
        except Exception as e:
            print(f'Ошибка при соединении {e}')
    client_socket.close()


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_socket:
        proxy_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        proxy_socket.bind((HOST, PORT))

        proxy_socket.listen(5)

        print('Прокси сервер запущен')

        is_running = True
        while is_running:
            client_socket, client_address = proxy_socket.accept()
            print(f'Подключение от {client_address}')

            thread = threading.Thread(target=handle_client, args=(client_socket,))
            thread.start()


if __name__ == '__main__':
    main()








