from pprint import pprint

import requests


def demo_redirects():
    response = requests.get("https://yandex.ru", allow_redirects=True)
    print("request:")
    print(response.request.headers)
    print(response.request.url)
    print(response.request)

    print("response:")
    print(response)
    print(" history:")
    for resp in response.history:
        print("---")
        print(resp.request.url)
        print(resp.url)
        print(resp.status_code)
        pprint(dict(resp.headers))
        print("===")

    print(response.status_code)
    pprint(dict(response.headers))
    print(response.text)


def demo_read_json():
    response = requests.get(
        "https://pie.dev/get",
        params={"foo": "bar", "fizz": "buzz"},
        headers={"user-agent": "PyCharm/2025xx"},
    )

    pprint(dict(response.headers))
    pprint(response.json())


def demo_send_json():
    response = requests.post(
        "https://pie.dev/post",
        params={"foo": "bar", "fizz": "buzz"},
        headers={"user-agent": "PyCharm/2025xx"},
        json={
            "platform": "OTUS",
            "lessons": [
                {
                    "id": "id-123",
                    "rating": 4.5,
                    "teacher": {
                        "name": "Suren",
                        "email": "suren@internet.ru",
                    },
                },
            ],
        }
    )

    pprint(dict(response.headers))
    pprint(response.json())


# demo_read_json()
demo_send_json()