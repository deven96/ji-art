release: python manage.py migrate
web: gunicorn django_photo_gallery.wsgi --log-file - --log-level debug
