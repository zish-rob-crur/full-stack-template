import rich

from backend_app.core.settings import Settings

settings = Settings()

rich.print_json(
    settings.model_dump_json(indent=2),
)
