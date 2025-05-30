import requests



url = 'https://jsonplaceholder.typicode.com/todos/1'

response = requests.get(url)

print(response)

if response.status_code == 200:
    print('OK')
    data = response.json()
    print(data)
    # print(response.text)
    print(data.get('title'))