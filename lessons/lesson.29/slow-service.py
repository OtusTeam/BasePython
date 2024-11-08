import asyncio

from aiohttp import web


async def hello(request: web.Request) -> web.Response:
    await asyncio.sleep(1)
    return web.json_response(text='{"message": "Hello World"}')


app = web.Application()
app.router.add_get("/", hello)

if __name__ == "__main__":
    web.run_app(app, host="127.0.0.1", port=8080)
