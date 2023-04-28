import asyncio

import aiohttp

URL_USERS = "https://jsonplaceholder.typicode.com/users"
URL_POSTS = "https://jsonplaceholder.typicode.com/posts"


async def get_response_data(url: str) -> list[dict] | dict | None | str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def async_main():
    # users: list[dict] = await get_response_data(URL_USERS)
    # posts: list[dict] = await get_response_data(URL_POSTS)
    users, posts = await asyncio.gather(
        get_response_data(URL_USERS),
        get_response_data(URL_POSTS),
    )

    print(users)
    print(posts)


if __name__ == "__main__":
    asyncio.run(async_main())
