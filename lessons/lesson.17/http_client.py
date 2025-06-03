import requests


# url = "https://httpbin.org/get"
# response = requests.get(url)
#
# print(response.status_code)
# print(response.text)

url = "https://httpbin.org/post"

data = {
    "name": "Ivan",
    "email": "ivan@mail.ru",
    "password": "123",
    "message": "Ivan send mail"
}

response = requests.post(url, data=data)

print(response.status_code)
print(response.text)