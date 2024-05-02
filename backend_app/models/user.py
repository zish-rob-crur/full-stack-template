from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Mapped

from backend_app.models.base import Base


class User(Base):
    __tablename__ = "users"

    name: Mapped[str] = Column(String, index=True)

    hashed_password: Mapped[str] = Column(String(length=128))
    email: Mapped[str] = Column(String, unique=True, index=True)
    is_active: Mapped[bool] = Column(String, default=True)
    is_superuser: Mapped[bool] = Column(String, default=False)

    def __repr__(self) -> str:
        return f"<User(name={self.name!r}, email={self.email!r})>"
