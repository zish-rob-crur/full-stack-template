#!/bin/bash

# Start the backend worker
celery -A backend_app.core.celery_app worker -l info 