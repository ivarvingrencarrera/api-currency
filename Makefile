SHELL := /bin/bash -O globstar

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

testing:
	docker compose up -d;
	pytest -x \
			--cov-report=term-missing --cov-report=html --cov-branch \
			--cov src/

testing_only:
	pytest -s -x -vv

install_hooks:
	@ scripts/install_hooks.sh

run:
	@python src/main_api.py

run_dev:
	@docker-compose up -d database; \
	trap 'docker-compose down' INT;


psql:
	@ docker compose exec -it postgres bash -c "psql -U root -d root"