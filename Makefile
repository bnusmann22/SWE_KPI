.PHONY: help install dev test lint format docker-up docker-down migrate seed init-db clean

help:
	@echo "KPI System - Available Commands"
	@echo "================================"
	@echo "make install      - Install dependencies"
	@echo "make dev          - Run development server"
	@echo "make test         - Run tests with coverage"
	@echo "make lint         - Run code linting"
	@echo "make format       - Format code with black and isort"
	@echo "make docker-up    - Start Docker services"
	@echo "make docker-down  - Stop Docker services"
	@echo "make migrate      - Run database migrations"
	@echo "make init-db      - Initialize database"
	@echo "make seed         - Seed sample data"
	@echo "make clean        - Clean up temporary files"

install:
	pip install -r requirements.txt -r requirements-dev.txt

dev:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

test:
	pytest tests/ -v --cov=app --cov-report=html --cov-report=term-missing

lint:
	flake8 app/ tests/
	mypy app/ --ignore-missing-imports

format:
	black app/ tests/ scripts/
	isort app/ tests/ scripts/

docker-up:
	docker-compose -f docker/docker-compose.yml up -d

docker-down:
	docker-compose -f docker/docker-compose.yml down

migrate:
	alembic upgrade head

init-db:
	python scripts/init_db.py

seed:
	python scripts/seed_data.py

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache .coverage htmlcov .mypy_cache
