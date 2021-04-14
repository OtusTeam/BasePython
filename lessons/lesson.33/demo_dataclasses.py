from dataclasses import dataclass


@dataclass
class User:
    id: int
    username: str
    is_staff: bool = False


u = User(id=1, username='admin', is_staff=True)
