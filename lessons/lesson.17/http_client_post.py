import http.client
import urllib.parse


my_dict = {
    "name": "John",
    "message": "Hello server!"
}

data = urllib.parse.urlencode(my_dict)

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": len(data)
}

connection = http.client.HTTPConnection("127.0.0.1", 8080)
connection.request('POST', '/', body=data, headers=headers)


response = connection.getresponse()
print(f'Статус: {response.status}')
print(f' {response.reason}')
for header in response.getheaders():
    print(f'{header}')

body = response.read().decode('utf-8')
print(f'Тело: {body}')

connection.close()
