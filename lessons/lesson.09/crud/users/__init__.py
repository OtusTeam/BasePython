__all__ = (
    "create",
    "update",
    "delete",
    "USERS_MAGIC_VARIABLE",
)

from .create import create
from .update import update
from .delete import delete
# from crud.users.create import create
# from crud.users.update import update
# from crud.users.delete import delete

USERS_MAGIC_VARIABLE = 42

print("users module (or package?), name:", repr(__name__))


def check():
    print("running users module (or package)")
