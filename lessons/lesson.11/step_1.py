import requests

url = 'https://otus.ru'
response = requests.get(url)
print(response.status_code)
content = response.content.decode()
# print(content)
with open('otus_2.html', 'w', encoding='utf-8') as f:
    f.write(content)
# f = open('otus_2.html', 'w', encoding='utf-8')
# f.write(content)
