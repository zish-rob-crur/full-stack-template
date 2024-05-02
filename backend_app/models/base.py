from datetime import datetime

from sqlalchemy import JSON, Column, Integer, DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm.decl_api import DeclarativeMeta


class Base(metaclass=DeclarativeMeta):
    __abstract__ = True
    __tablename__: str

    id: Mapped[int] = Column(Integer, primary_key=True, index=True)

    created_at: Mapped[datetime] = Column(
        DateTime,
        default=datetime.now,
        index=True,
    )
    updated_at: Mapped[datetime] = Column(
        DateTime, default=datetime.now, onupdate=datetime.now, index=True
    )
    metadata: Mapped[dict] = Column(
        JSON,
    )
