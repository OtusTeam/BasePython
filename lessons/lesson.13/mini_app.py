# from pprint import pprint


def application(environ, start_response):
    # print("environ:")
    # pprint(environ)
    data = b"Hello, World!\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data))),
        # ("X-Extra-id", "123456"),
    ])
    return iter([data])
