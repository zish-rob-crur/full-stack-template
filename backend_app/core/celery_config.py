from backend_app.core import settings

broker_url = str(settings.celery.broker_url)
result_backend = str(settings.celery.result_backend)
celery_task_serializer = settings.celery.task_serializer
celery_result_serializer = settings.celery.result_serializer
celery_accept_content = settings.celery.accept_content

celery_worker_concurrency = settings.celery.worker_concurrency
celery_worker_prefetch_multiplier = settings.celery.worker_prefetch_multiplier
celery_worker_max_tasks_per_child = settings.celery.worker_max_tasks_per_child


include = [
    "backend_app.tasks.user",
    "backend_app.tasks.x_downloader.downloader"
]
