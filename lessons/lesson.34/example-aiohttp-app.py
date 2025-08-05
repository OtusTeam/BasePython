import asyncio
from typing import Any

from aiohttp import web
import random


# Function to generate user data
async def generate_user_data(user_id):
    # # FOR EXAMPLE:
    # очень медленно грузится апишка. синтетический пример
    await asyncio.sleep(0.5)
    # Sample user data
    user_data = {
        "user_id": user_id,
        "age": random.randint(18, 60),
        "location": random.choice(
            [
                "Moscow",
                "Saint Petersburg",
                "Novosibirsk",
                "Yekaterinburg",
            ],
        ),
    }
    return user_data


# API handler for /user-info/{user_id}
async def user_info(request: web.Request) -> web.Response:
    user_id = request.match_info.get("user_id")
    user_data: dict[str, Any] = await generate_user_data(user_id)
    return web.json_response(user_data)


# Create the application
app = web.Application()
app.router.add_get(
    "/user-info/{user_id}",
    user_info,
)

# Run the application
if __name__ == "__main__":
    web.run_app(app, host="127.0.0.1", port=5000)
