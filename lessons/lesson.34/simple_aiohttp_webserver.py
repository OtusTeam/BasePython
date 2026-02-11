import asyncio
import json
import logging
import random
import string

from aiohttp import web


def random_string(length=8):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


def random_payload(user_id: str):
    return {
        "user_id": user_id,
        "token": random_string(24),
        "score": round(random.uniform(0, 100), 2),
        "active": random.choice([True, False]),
        "tags": random.sample(
            ["alpha", "beta", "gamma", "delta", "epsilon"],
            k=random.randint(1, 3),
        ),
    }


async def handle(request):
    user_id = request.match_info.get("user_id")
    try:
        data = await request.json()
    except json.JSONDecodeError:
        return web.json_response(
            {"error": "invalid json"},
            status=400,
        )

    logging.debug("data: %s", data)
    # optionally do something with incoming JSON `data`
    # generate random response based on user_id
    resp = random_payload(user_id)
    resp["incoming"] = data
    await asyncio.sleep(0.2)
    return web.json_response(resp)


app = web.Application()
app.router.add_post("/api/{user_id}", handle)

if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=5050)
