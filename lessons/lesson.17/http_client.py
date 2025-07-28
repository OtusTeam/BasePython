import email

import requests


# url = "http://127.0.0.1:8000/home"

# url = "https://httpbin.org/get"
# response = requests.get(url)
# print(response.status_code)
# print(response.text)


# url = "https://httpbin.org/post"
#
# data = {
#     "name": "Ivan",
#     "email": "ivan@mail.com",
#     "password": "123",
#     "message": "Hello, Ivan!",
# }
# response = requests.post(url, data=data)
# print(response.status_code)
# print(response.text)


url = "http://127.0.0.1:8081/home"

data = {
    "name": "Ivan",
    "email": "ivan@mail.com",
    "password": "123",
    "message": "Hello, Ivan!",
}
response = requests.post(url, data=data)
print(response.status_code)
print(response.text)