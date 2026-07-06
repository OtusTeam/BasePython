from pydantic import BaseModel


class AppConfig(BaseModel):
    title: str = "Blog"
