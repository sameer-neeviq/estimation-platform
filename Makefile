.PHONY: help install dev-up dev-down test lint format clean migrate upgrade

help:
	@echo "Available commands:"
	@echo "  install     - Install dependencies"
	@echo "  dev-up      - Start development environment"
	@echo "  dev-down    - Stop development environment"
	@echo "  test        - Run tests"
	@echo "  lint        - Run linting"
	@echo "  format      - Format code"
	@echo "  clean       - Clean up containers and volumes"
	@echo "  migrate     - Generate new migration"
	@echo "  upgrade     - Apply migrations"

install:
	pip install -r requirements.txt

dev-up:
	docker-compose -f docker-compose.dev.yml up --build

dev-down:
	docker-compose -f docker-compose.dev.yml down

test:
	pytest tests/ -v

lint:
	flake8 app/ tests/
	mypy app/

format:
	black app/ tests/
	isort app/ tests/

clean:
	docker-compose -f docker-compose.dev.yml down -v
	docker system prune -f

migrate:
	alembic revision --autogenerate -m "$(msg)"

upgrade:
	alembic upgrade head
