release: sh -c 'python manage.py migrate && python manage.py loaddata initial_catalog_data.json && python manage.py loaddata initial_watchlist.json'
web: gunicorn project_django.wsgi --log-file -