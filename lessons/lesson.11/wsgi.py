def application(environ, start_response):
    print(environ)
    # business logic
    start_response('200', [('Content-Type', 'text/plain')])
    yield b'Hello, World!\n'
