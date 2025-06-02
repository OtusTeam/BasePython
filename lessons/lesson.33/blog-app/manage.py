from typing import Annotated

import typer

from api.api_v1.users.crud import UsersCRUD
from models.db import session_factory

from rich import print


app = typer.Typer(
    no_args_is_help=True,
)


@app.callback()
def callback():
    """
    Commands
    """


@app.command()
def create_users(
    n_users: Annotated[
        int,
        typer.Argument(
            help="Number of users to create",
        ),
    ],
) -> None:
    """
    Create users in DB
    """
    print("[bold]Creating users...[/bold]")
    with session_factory() as session:
        crud = UsersCRUD(session)
        crud.crete_n_users(n_users)

    print(f"[green]Created {n_users} users[/green]")


if __name__ == "__main__":
    app()
