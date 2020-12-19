from .base import BaseModel
from .user import User
from .article import Article


class BaseModelOld:
    pass


# print("models init name", __name__)
# print("models init file", __file__)

__all__ = [
    "User",
    "Article",
]
