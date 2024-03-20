from pprint import pprint


def application(environ, start_response):
    print("===" * 10)
    pprint(environ)
    print("===" * 10)

    data = b"Hello, OTUS!\n"
    start_response(
        "200 OK",
        [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data))),
        ],
    )
    return iter([data])
