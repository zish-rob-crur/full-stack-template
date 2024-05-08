from backend_app.db import Session
from backend_app.models import User
from backend_app.core.security import get_password_hash


def create_user(
    username: str,
    password: str,
    is_superuser: bool = False,
) -> User:
    hashed_password = get_password_hash(password)
    with Session() as session:
        user = User(
            name=username,
            hashed_password=hashed_password,
            is_superuser=is_superuser,
        )
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
