from loguru import logger
from fastapi import APIRouter

from backend_app.tasks.user import create_user, send_user_hello_email

router = APIRouter(
    tags=["user"],
)


@router.get("/users/me")
def read_users_me():
    return {"username": "fakecurrentuser"}


@router.post("/users/")
def create_user_route(
    username: str,
    password: str,
):
    workflow = create_user.s(username, password) | send_user_hello_email.s()
    async_result = workflow.apply_async()
    logger.info("create_user_route task_id: {async_result.id}")
    return {"task_id": async_result.id}

