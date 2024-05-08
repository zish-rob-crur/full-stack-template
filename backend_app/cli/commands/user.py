import typer

app = typer.Typer()


@app.command()
def create_user(
    username: str = typer.Argument(..., help="Username"),
    password: str = typer.Argument(..., help="Password"),
    superuser: bool = typer.Option(False, help="Create superuser"),
):
    from backend_app.crud.user import create_user as crud_create_user

    user = crud_create_user(username, password, is_superuser=superuser)
    typer.echo(f"User {user.name} created id {user.id}")


@app.command()
def list_users():
    pass
