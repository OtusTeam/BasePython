"""
gunicorn -w 1 web:app
"""


def app(environ, start_response):
    data = b"<h1>Hello, World!</h1>\n"
    start_response("200 OK", [
        ("Content-Type", "text/html"),
        ("Content-Length", str(len(data))),
    ])
    return iter([data])
    # yield data
