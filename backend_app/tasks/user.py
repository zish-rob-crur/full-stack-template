from loguru import logger

from backend_app.core import settings
from backend_app.core.celery_app import app


@app.task()
def create_user(
    username: str,
    password: str,
):
    logger.info(
        "get task create_user with username: {username}",
    )
    return username


@app.task()
def send_user_hello_email(username: str):
    logger.info(
        "get task send_user_hello_email with username: {username}",
    )
    return username

