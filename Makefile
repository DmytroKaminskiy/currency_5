SHELL := /bin/bash

manage_py := docker exec -it backend python app/manage.py

build:
	cp -n .env.example .env && docker-compose up -d --build

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

pytest:
	 pytest ./app/tests/ --cov=app --cov-report html && coverage report --fail-under=74

show-coverage:  ## open coverage HTML report in default browser
	python3 -c "import webbrowser; webbrowser.open('.pytest_cache/coverage/index.html')"
