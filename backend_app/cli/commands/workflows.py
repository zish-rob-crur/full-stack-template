import typer

app = typer.Typer()


@app.command()
def _start_download_workflow():
    from backend_app.tasks.x_downloader.downloader import (
        create_download_workflow,
    )

    return create_download_workflow()
