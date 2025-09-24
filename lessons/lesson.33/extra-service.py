import asyncio
import random
import string
from aiohttp import web


def random_string(length=8):
    return "".join(
        random.choices(
            string.ascii_letters + string.digits,
            k=length,
        ),
    )


def random_email(name_hint=None):
    name = (name_hint or random_string(6)).lower()
    domains = ["example.com", "mail.com", "test.org"]
    return f"{name}@{random.choice(domains)}"


async def handle_get_user(request):
    user_id = request.match_info.get("user_id")

    # имитируем долгое ожидание
    await asyncio.sleep(0.5)

    # random data
    profile = {
        "id": user_id,  # echo back the id
        "name": random_string(10),
        "email": random_email(user_id),
        "age": random.randint(18, 80),
        # three extra fields
        "extra_1": random.choice(["alpha", "beta", "gamma"]),
        "extra_2": round(random.uniform(0, 100), 2),
        "extra_3": {"flag": random.choice([True, False]), "notes": random_string(20)},
    }

    return web.json_response(profile)


def create_app():
    app = web.Application()
    app.router.add_get("/users/{user_id}", handle_get_user)
    return app


def main():
    app = create_app()
    web.run_app(
        app,
        host="0.0.0.0",
        port=5050,
    )


if __name__ == "__main__":
    main()
