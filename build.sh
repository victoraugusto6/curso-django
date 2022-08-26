#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

#export DJANGO_SUPERUSER_EMAIL=victor.augusto.soliveira@gmail.com
#export DJANGO_SUPERUSER_PASSWORD=deployinrender
#python manage.py createsuperuser --no-input

python manage.py collectstatic --no-input
python manage.py migrate
