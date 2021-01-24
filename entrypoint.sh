#!/bin/sh
set -e

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    sleep 5
fi

# Flush will remove all data handle with care
# python manage.py flush --no-input

python manage.py migrate
python manage.py collectstatic --no-input

exec "$@"