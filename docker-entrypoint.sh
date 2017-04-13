#!/bin/sh
# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput
NUM_WORKERS=${1:-3}
BIND=${2:-0.0.0.0:8000}
# Start server
echo "Starting server"
exec gunicorn sitebeldsi.wsgi:application \
 --workers $NUM_WORKERS \
 --bind=$BIND \
 --log-file=logs/gunicorn.log