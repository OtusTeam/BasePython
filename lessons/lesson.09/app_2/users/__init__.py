__all__ = (
    "create",
    "update",
    "delete",
    "USERS_MAGIC_VARIABLE",
)

# from .create import create
# from .update import update
# from .delete import delete
from users.create import create
from users.update import update
from users.delete import delete

USERS_MAGIC_VARIABLE = 42


def check():
    print("users module (or package?), name:", repr(__name__))


check()

