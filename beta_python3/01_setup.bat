#!/bin/sh

python manage.py makemigrations
python manage.py migrate --run-syncdb
python manage.py createsuperuser
python manage.py shell_plus --notebook
