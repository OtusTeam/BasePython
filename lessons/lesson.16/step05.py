import requests


url = "https://httpbin.org/get"

headers = {
    'User-Agent': "MyOtus",
    'Token_OTUS': '1234567qwerty'
}

response = requests.get(url, headers=headers)
# response = requests.post(url)
# response = requests.put(url)
# response = requests.delete(url)


if response:
    print(response.headers)
    print('*' * 50)
    my_text = response.text
    print(my_text)
    print(type(my_text))
    print('*' * 50)
    my_content = response.content
    print(my_content)
    print(type(my_content))
else:
    print('NO')