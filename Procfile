web: gunicorn sked-evento.wsgiweb:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate
web: python manage.py runserver
