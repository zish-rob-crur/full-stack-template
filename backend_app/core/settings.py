from pydantic import MySQLDsn, RedisDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class LogSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="LOG_")
    level: str = "INFO"
    path: str = "logs/app.log"
    serialize: bool = False
    rotation: str = "1 week"


class DbSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="DB_")
    url: MySQLDsn = "mysql://user:password@localhost/db"
    pool_size: int = 10


class CacheSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="CACHE_")
    url: RedisDsn = "redis://localhost"
    pool_size: int = 10


class CelerySettings(BaseSettings):
    broker_url: RedisDsn = "redis://localhost"
    result_backend: RedisDsn = "redis://localhost"

    task_serializer: str = "json"
    result_serializer: str = "json"
    accept_content: list[str] = ["json", "pickle"]
    worker_concurrency: int = 10
    worker_prefetch_multiplier: int = 1
    worker_max_tasks_per_child: int = 100


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    secret_key: str = "secret"
    db: DbSettings = DbSettings()
    cache: CacheSettings = CacheSettings()
    celery: CelerySettings = CelerySettings()
    log: LogSettings = LogSettings()