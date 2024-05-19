import typer

from backend_app.cli.commands import user, workflows

app = typer.Typer()
app.add_typer(user.app, name="user")
app.add_typer(workflows.app, name="workflows")

if __name__ == "__main__":
    app()
