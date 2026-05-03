# Шпаргалка: Как работает сервер

## 🖥️ socket - Работа с сокетами

### Создание сервера:
```python
import socket

# Создать сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязать к адресу и порту
server_socket.bind(('localhost', 8080))

# Слушать подключения
server_socket.listen(5)

# Принять подключение
client_socket, address = server_socket.accept()

# Отправить данные
client_socket.send(b'HTTP/1.1 200 OK\r\n\r\nHello World!')

# Закрыть
client_socket.close()
server_socket.close()
```

### Создание клиента:
```python
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8080))
client_socket.send(b'GET / HTTP/1.1\r\n\r\n')
response = client_socket.recv(1024)
client_socket.close()
```

---

## 🌐 HTTP Сервер

### Простой HTTP сервер:
```python
import socket

def create_http_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 8080))
    server.listen(5)
    
    while True:
        client, addr = server.accept()
        request = client.recv(1024).decode()
        
        # Парсинг запроса
        method = request.split()[0]
        path = request.split()[1]
        
        # Формирование ответа
        if path == '/':
            response = 'HTTP/1.1 200 OK\r\n\r\n<h1>Home Page</h1>'
        elif path == '/hello':
            response = 'HTTP/1.1 200 OK\r\n\r\n<h1>Hello World!</h1>'
        else:
            response = 'HTTP/1.1 404 Not Found\r\n\r\n<h1>Page Not Found</h1>'
        
        client.send(response.encode())
        client.close()
```

---

## 🔄 Прокси-сервер

### Простой прокси:
```python
import socket
import threading

def handle_client(client_socket):
    # Получить запрос от клиента
    request = client_socket.recv(1024)
    
    # Извлечь URL из запроса
    first_line = request.decode().split('\n')[0]
    url = first_line.split()[1]
    
    # Подключиться к целевому серверу
    http_pos = url.find("://")
    if http_pos == -1:
        temp = url
    else:
        temp = url[(http_pos + 3):]
    
    port_pos = temp.find(":")
    webserver_pos = temp.find("/")
    
    if webserver_pos == -1:
        webserver_pos = len(temp)
    
    webserver = temp[:webserver_pos]
    port = 80
    
    # Создать сокет для целевого сервера
    proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxy_socket.connect((webserver, port))
    proxy_socket.send(request)
    
    # Получить ответ и переслать клиенту
    data = proxy_socket.recv(1024)
    client_socket.send(data)
    
    proxy_socket.close()
    client_socket.close()

def start_proxy():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 8888))
    server.listen(5)
    
    while True:
        client, addr = server.accept()
        threading.Thread(target=handle_client, args=(client,)).start()
```

---

## 📧 smtplib - Отправка почты

### Основные функции:
```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Создание сообщения
msg = MIMEMultipart()
msg['From'] = 'sender@example.com'
msg['To'] = 'recipient@example.com'
msg['Subject'] = 'Тема письма'

# Добавление текста
body = 'Текст письма'
msg.attach(MIMEText(body, 'plain'))

# Отправка через Gmail
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # Включить шифрование
    server.login('your_email@gmail.com', 'your_password')
    server.send_message(msg)
    server.quit()
    print("Письмо отправлено!")
except Exception as e:
    print(f"Ошибка: {e}")
```

### Простая отправка:
```python
import smtplib

def send_simple_email(to_email, subject, message):
    from_email = "your_email@gmail.com"
    password = "your_password"
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    
    email_text = f"""
    From: {from_email}
    To: {to_email}
    Subject: {subject}
    
    {message}
    """
    
    server.sendmail(from_email, to_email, email_text)
    server.quit()
```

---

## 🔗 Интеграция: Прокси + Email логгер

### Прокси с логированием на почту:
```python
import socket
import smtplib
import threading
import datetime

def log_to_email(message):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('logger@gmail.com', 'password')
        
        email_text = f"""
        From: logger@gmail.com
        To: admin@gmail.com
        Subject: Proxy Log
        
        {datetime.datetime.now()}: {message}
        """
        
        server.sendmail('logger@gmail.com', 'admin@gmail.com', email_text)
        server.quit()
    except Exception as e:
        print(f"Ошибка отправки лога: {e}")

def proxy_with_logging():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 8888))
    server.listen(5)
    
    while True:
        client, addr = server.accept()
        
        # Логирование подключения
        log_message = f"Новое подключение от {addr}"
        log_to_email(log_message)
        
        threading.Thread(target=handle_client_with_log, args=(client, addr)).start()
```

---

## 🛠️ Полезные паттерны

### HTTP статус коды:
```python
HTTP_STATUS = {
    200: 'OK',
    404: 'Not Found',
    500: 'Internal Server Error',
    403: 'Forbidden',
    301: 'Moved Permanently'
}

def create_response(status_code, body):
    status_text = HTTP_STATUS.get(status_code, 'Unknown')
    return f'HTTP/1.1 {status_code} {status_text}\r\n\r\n{body}'
```

### Многопоточный сервер:
```python
import threading

def handle_client(client_socket, address):
    # Обработка клиента
    pass

def start_threaded_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 8080))
    server.listen(5)
    
    while True:
        client, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(client, addr))
        thread.start()
```

---

## ⚠️ Важные моменты

- Всегда закрывайте сокеты (`socket.close()`)
- Используйте `try/except` для обработки ошибок сети
- Для production используйте готовые фреймворки (Flask, FastAPI)
- Помните про безопасность при работе с прокси
- Используйте SSL/TLS для шифрования
- Не храните пароли в коде (используйте переменные окружения) 