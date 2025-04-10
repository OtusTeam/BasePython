from typing import Annotated
import typer

from api.api_v1.users.crud import UsersCRUD
from models.db import session_factory

app = typer.Typer(
    no_args_is_help=True,
)


@app.callback()
def callback():
    """
    Commands to work with our app.
    """


@app.command()
def create_users(
    n_users: Annotated[
        int,
        typer.Argument(
            help="Number of users to create",
        ),
    ],
):
    """
    Create new users in Database.
    """
    with session_factory() as session:
        crud = UsersCRUD(session)
        users = crud.create_n_users(n_users)

    print(f"Done. Created {len(users)} users.")


if __name__ == "__main__":
    app()
