#!/bin/sh
gunicorn --chdir app --workers 4 --threads 2 -b 0.0.0.0:5000
#gunicorn -p gunicorn.pid --workers $GUNICORN_WORKERS --threads $GUNICORN_THREADS --worker-class $GUNICORN_WORKER_CLASS --log-level $GUNICORN_LOG_LEVEL --max-requests=$GUNICORN_MAX_REQUESTS --max-requests-jitter $GUNICORN_RESTART_JITTER --worker-connections $GUNICORN_WORKER_CONNECTIONS --timeout $GUNICORN_WORKER_TIMEOUT --bind=0.0.0.0:5000 demo:app