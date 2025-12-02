"""

# aiohttp server:
# - accepts POST request to /api/users/{user_id}/
# - returns user data dict with same id, random postal address
# - runs app on port 5050
"""

import asyncio
from aiohttp import web
from faker import Faker

# Initialize Faker for generating random data
fake = Faker()


async def handle_user_post(request: web.Request) -> web.Response:
    """
    Handles POST requests to /api/users/{user_id}/
    Extracts user_id from the URL and generates a random address.
    """
    # Extract the user_id from the URL path parameters
    user_id = request.match_info.get("user_id")

    # Generate a random postal address
    random_address = fake.address()

    # Create the response data dictionary
    user_data = {
        "user_id": user_id,
        "postal_address": random_address,
    }
    await asyncio.sleep(0.2)

    # Return the data as a JSON response
    return web.json_response(user_data)


async def init_app() -> web.Application:
    """
    Initializes the aiohttp application and sets up routes.
    """
    application = web.Application()
    # Define the POST route with a variable path parameter {user_id}
    application.router.add_post("/api/users/{user_id}/", handle_user_post)
    return application


app = init_app()

if __name__ == "__main__":
    # Run the application on the specified port
    # The port is passed as an argument to web.run_app
    web.run_app(app, port=5050)
