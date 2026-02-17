from pydantic import BaseModel


class HttpConfig(BaseModel):
    proxy: bool = False
