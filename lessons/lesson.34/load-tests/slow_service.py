"""
gunicorn slow_service:app --workers 4 --worker-class aiohttp.GunicornWebWorker --bind 0.0.0.0:3000
"""

import asyncio

from aiohttp import web

routes = web.RouteTableDef()


@routes.get("/get-data")
async def hello(request):
    await asyncio.sleep(0.1)
    return web.json_response(
        data={
            "name": "John Doe",
            "age": 30,
            "is_student": False,
            "courses": [
                "Math",
                "Science",
                "History",
                "English",
                "Art",
                "Physical Education",
                "Computer Science",
                "Biology",
                "Chemistry",
                "Physics",
            ],
            "address": {
                "street": "123 Main St",
                "city": "Anytown",
                "state": "CA",
                "zip": "12345",
                "country": "USA",
                "latitude": 34.0522,
                "longitude": -118.2437,
            },
            "graduation_year": None,
            "hobbies": [
                "Reading",
                "Traveling",
                "Gaming",
                "Cooking",
                "Hiking",
                "Photography",
                "Music",
                "Drawing",
                "Writing",
                "Volunteering",
            ],
            "employment": {
                "current_job": {
                    "title": "Software Developer",
                    "company": "Tech Solutions",
                    "years_experience": 5,
                },
                "previous_jobs": [
                    {
                        "title": "Intern",
                        "company": "Web Innovations",
                        "duration_months": 6,
                    },
                    {
                        "title": "Junior Developer",
                        "company": "Code Factory",
                        "duration_months": 12,
                    },
                ],
            },
            "skills": {
                "programming_languages": ["Python", "JavaScript", "Java", "C++"],
                "frameworks": ["Django", "Flask", "React", "Angular"],
                "databases": ["MySQL", "PostgreSQL", "MongoDB"],
            },
        },
    )


app = web.Application()
app.add_routes(routes)

if __name__ == "__main__":
    web.run_app(app)
