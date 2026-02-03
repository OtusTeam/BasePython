from fastapi import FastAPI, Response
from starlette import status

from config.settings import settings

app = FastAPI()


@app.get("/hello")
def hello(name: str = "World") -> dict[str, str]:
    return {
        "message": f"Hello, {name}!",
    }


# @app.get(
#     "/all-settings",
# )
# def get_settings(
#     response: Response,
# ):
#     """
#     ТОЛЬКО ДЛЯ ДЕМО
#     НИКОГДА НЕ ОТДАЁМ НАСТРОЙКИ
#     """
#     response.headers["Content-Type"] = "application/json"
#     response.body = settings.model_dump_json(indent=2).encode("utf-8")
#     response.status_code = status.HTTP_200_OK
#     return response


if __name__ == "__main__":
    print(settings.model_dump_json(indent=2))
