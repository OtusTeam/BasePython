import asyncio
from http import HTTPStatus

from aiohttp import web
import json


async def reverse_user_id(request: web.Request) -> web.Response:
    try:
        data = await request.json()
    except json.JSONDecodeError:
        return web.json_response(
            {"error": "Invalid JSON"},
            status=HTTPStatus.BAD_REQUEST,
        )

    raw_user_id: str | None = data.get("user_id")
    if raw_user_id is None:
        return web.json_response(
            {"error": "user_id is required"},
            status=HTTPStatus.BAD_REQUEST,
        )
    if not (
        isinstance(raw_user_id, int)
        or isinstance(raw_user_id, str)
        and raw_user_id.isdigit()
    ):
        return web.json_response(
            {"error": "user_id must be an integer"},
            status=HTTPStatus.BAD_REQUEST,
        )
    user_id = int(raw_user_id)
    reversed_user_id = 0
    while user_id:
        reversed_user_id = reversed_user_id * 10 + user_id % 10
        user_id //= 10
    await asyncio.sleep(0.3)
    return web.json_response({"reversed_user_id": reversed_user_id})


app = web.Application()
app.router.add_post("/reverse-id", reverse_user_id)

if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=8888)
