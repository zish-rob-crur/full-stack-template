from typing import ContextManager
from contextlib import contextmanager

import redis
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from backend_app.core import settings

Engine = create_engine(
    settings.db.url,
    pool_size=settings.db.pool_size,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)
RedisPool = redis.ConnectionPool.from_url(
    settings.cache.url,
    max_connections=settings.cache.pool_size,
)


@contextmanager
def get_db_session() -> ContextManager[Session]:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def get_redis() -> redis.Redis:
    return redis.Redis(connection_pool=RedisPool)
