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
	pytest --cov-report term-missing --cov-report html --cov-branch --cov src/

testing_only:
	pytest -s -x -vv

install_hooks:
	@ scripts/install_hooks.sh