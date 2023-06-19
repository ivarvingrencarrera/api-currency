SHELL := /bin/bash -O globstar

run_dev: check_env
		@docker-compose up -d database; \
		trap 'docker-compose down' INT;
		

testing: check_env
		docker compose up -d database;
		pytest --cov-report=term-missing --cov-report=html --cov-branch --cov src/;
		docker compose down;


linting:
		@echo
		isort . 
		@echo
		ruff .
		@echo
		blue --check --diff --color . 
		@echo
		mypy . 
		@echo
		pip-audit


formating:
		isort .
		ruff --silent --exit-zero --fix .
		blue .


install_hooks:
		@scripts/install_hooks.sh


run:
		@python src/main_api.py


build:
		docker build -t api-currency .


psql:
		@docker compose exec -it postgres bash -c "psql -U root -d root"


check_env:
		@if [ ! -f ".env" ]; then cp sample.env .env; fi