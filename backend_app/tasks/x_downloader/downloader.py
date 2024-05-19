import time
from typing import List

from loguru import logger
from pydantic import BaseModel

from backend_app.db import Session
from backend_app.core.celery_app import app


class DownloadTask(BaseModel):
    db_id: int
    download_url: str
    status: str = "PENDING"


@app.task()
def get_db_download_task() -> List[DownloadTask]:
    with Session() as session:
        result = session.execute(
            "SELECT id, download_url FROM download_task WHERE status = 'PENDING'"
        )
        return [
            DownloadTask(db_id=db_id, download_url=download_url)
            for db_id, download_url in result
        ]


@app.task()
def download_file(download_task: DownloadTask):
    # Download the file and update the status in the database
    logger.info(f"Downloaded file from {download_task.download_url}")
    time.sleep(5)
    download_task.status = "COMPLETED"
    return download_task


@app.task()
def set_download_success_status(download_task: DownloadTask):
    with Session() as session:
        session.execute(
            "UPDATE download_task SET status = :status WHERE id = :db_id",
            {"status": "COMPLETED", "db_id": download_task.db_id},
        )
        session.commit()


@app.task()
def set_download_failed_status(
    request,
    exc,
    traceback,
    download_task: DownloadTask,
):
    with Session() as session:
        session.execute(
            "UPDATE download_task SET status = 'FAILED' WHERE id = :db_id",
            {"db_id": download_task.db_id},
        )
        session.commit()


def create_download_workflow():
    """
    1. query the database for pending download tasks
    2. submit a download task for each pending task to download the file
        2.1 link the download task to the database task
    """

    download_tasks = get_db_download_task()
    logger.info(f"Found {len(download_tasks)} pending download tasks")
    for download_task in download_tasks:
        flow = download_file.apply_async(
            args=[download_task],
            link_error=set_download_failed_status.s(download_task),
            link=set_download_success_status.s(download_task),
        )
        logger.info(f"Submitted download task {flow.id} for {download_task.db_id}")
