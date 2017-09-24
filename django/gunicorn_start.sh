python manage.py collectstatic --no-input
python manage.py migrate
gunicorn --bind 0.0.0.0:4431 hanashiai.wsgi