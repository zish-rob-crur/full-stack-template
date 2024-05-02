# !/bin/bash

PORT=${PORT:-8000}
APP_ENV=${APP_ENV:-dev}
HOST=${HOST:-127.0.0.1}
WORKERS=${WORKERS:-4}
LOG_LEVEL=${LOG_LEVEL:-debug}

if [ "$APP_ENV" == "prod" ]; then
    HOST="0.0.0.0"
    LOG_LEVEL="info"
fi

# Start the backend
echo "Starting backend server..."

cmd="gunicorn -b $HOST:$PORT \
--log-level=$LOG_LEVEL \
--log-file=- \
--workers=$WORKERS \
--worker-class=uvicorn.workers.UvicornWorker backend_app.service.main:app"

if [ "$APP_ENV" == "dev" ]; then
    $cmd --reload
else
    $cmd
fi
