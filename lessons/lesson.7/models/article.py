from .base import BaseModel


class Article(BaseModel):

    def change_author(self):
        from .user import User
        print(User)

    def process_author(self):
        from .user import User
