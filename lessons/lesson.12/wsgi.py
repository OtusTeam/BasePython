def app(environ, start_response):
    # print("env:", environ)
    response_data = b"Hello, John!"
    start_response(
        "200 OK",
        [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(response_data)))
        ],
    )
    yield response_data
