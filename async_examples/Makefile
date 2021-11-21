SHELL := /bin/bash

#run-dev:
#	uvicorn main:app --reload --host=0.0.0.0 --port=8081

makemigrations:
	docker exec -it backend alembic revision --autogenerate -m "Added required tables"

migrate:
	docker exec -it backend alembic upgrade head
