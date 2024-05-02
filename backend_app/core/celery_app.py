from celery import Celery

from backend_app.core import celery_config

app = Celery("backend_app")
app.config_from_object(celery_config)

