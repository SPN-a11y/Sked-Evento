web: gunicorn Sked-Evento.wsgiweb:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate
web: gunicorn --bind 0.0.0.0:$PORT Sked-Evento:app
