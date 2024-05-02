from fastapi import APIRouter

from backend_app.service.api.v1 import user

router = APIRouter(
    prefix="/api/v1",
)

router.include_router(user.router, prefix="/user")
