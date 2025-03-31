# curl -x http://127.0.0.1:8888 http://mail.ru/search2

import requests

proxies = {
    'http': 'http://127.0.0.1:8888',
    # 'https': 'https://127.0.0.1:8888',
}


# response = requests.get('http://mail.ru/search', proxies=proxies)
response = requests.get('http://example.com', proxies=proxies)

print(response.status_code)
print(response.text)