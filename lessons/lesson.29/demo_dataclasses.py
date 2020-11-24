from dataclasses import dataclass


@dataclass
class User:
    id: int
    username: str
    is_staff: bool = False


u = User(id=1, username="john")
admin = User(id=42, username="admin", is_staff=True)

print("user", u)
print("admin", admin)
