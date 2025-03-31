import http.client
import urllib.parse


connection = http.client.HTTPConnection("127.0.0.1", 8080)
connection.request('GET', '/')

response = connection.getresponse()
print(f'Статус: {response.status}')
print(f' {response.reason}')
for header in response.getheaders():
    print(f'{header}')

body = response.read().decode('utf-8')
print(f'Тело: {body}')

connection.close()
