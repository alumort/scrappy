.PHONY: build up down logs restart \
        migrate migrations shell createsuperuser bash test \
        tailwind-logs psql

build:
	docker compose build

up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f

restart:
	docker compose restart web

migrate:
	docker compose exec web python manage.py migrate

migrations:
	docker compose exec web python manage.py makemigrations

shell:
	docker compose exec web python manage.py shell

createsuperuser:
	docker compose exec web python manage.py createsuperuser

bash:
	docker compose exec web /bin/bash

test:
	docker compose exec web python manage.py test

seed:
	docker compose exec web python manage.py seed

tailwind-logs:
	docker compose logs -f tailwind

psql:
	docker compose exec db psql -U $$DB_USER -d $$DB_NAME

wipe-vol:
	docker compose down -v