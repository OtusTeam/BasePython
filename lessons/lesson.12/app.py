def app(environ, start_response):
    data = "Hello, World! 🤯\n".encode("utf-8")
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data))),
    ])
    print(environ.get("PATH_INFO"))
    return iter([data])
