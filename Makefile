SHELL := /bin/bash

manage_py := python app/manage.py

runserver:
	$(manage_py) runserver 0:8000

migrate:
	$(manage_py) migrate

makemigrations:
	$(manage_py) makemigrations

shell:
	$(manage_py) shell_plus --print-sql

show_urls:
	$(manage_py) show_urls

createsuperuser:
	$(manage_py) createsuperuser

gunicorn:
	cd app && gunicorn settings.wsgi:application --workers 4 --bind 0.0.0.0:8001 --threads 4 --timeout 3 --max-requests 1000 --log-level debug

worker:
	cd app && celery -A settings worker -l info --autoscale=10,0
	#cd app && celery -A settings worker -l info --concurrency 20
    # prefork - Process
    # gevent - Thread

beat:
	cd app && celery -A settings beat -l info

pytest:
	 pytest ./app/tests/ --cov=app --cov-report html && coverage report --fail-under=74

show-coverage:  ## open coverage HTML report in default browser
	python3 -c "import webbrowser; webbrowser.open('.pytest_cache/coverage/index.html')"