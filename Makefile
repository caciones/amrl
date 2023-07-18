include .env
export

build:
	DOCKER_BUILDKIT=1 docker build --no-cache --rm -t amrl:latest .

down:
	docker compose down

start: down
	docker compose up -d

server:
	python manage.py runserver

migrate:
	python manage.py migrate

createsuperuser:
	python manage.py createsuperuser

run:
	docker run --env-file .env -p 8000:8000 amrl:latest

shell:
	docker run --env-file .env -p 8000:8000 -ti amrl:latest bash

dump:
	python manage.py dumpdata > data.json

load:
	python manage.py loaddata data.json
