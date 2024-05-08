import typer

from backend_app.cli.commands import user

app = typer.Typer()
app.add_typer(user.app, name="user")

if __name__ == "__main__":
    app()
