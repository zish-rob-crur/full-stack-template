from pathlib import Path

from loguru import logger

from backend_app.core import settings

if not (path := Path(settings.log.path)).parent.exists():
    path.parent.mkdir(parents=True)

logger.add(
    settings.log.path,
    rotation=settings.log.rotation,
    level=settings.log.level,
    serialize=settings.log.serialize,
)
