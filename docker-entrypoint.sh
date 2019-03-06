#!/bin/bash

bash scripts/tcp-port-wait.sh $DATABASE_HOST $DATABASE_PORT

echo $(date -u) " - Migrating"
python manage.py migrate

echo $(date -u) "- Running the server"
gunicorn -b 0.0.0.0:8080 documents-service.wsgi
