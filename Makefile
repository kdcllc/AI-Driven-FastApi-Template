.PHONY: help install dev test lint format clean run

help:
	@echo "Available commands:"
	@echo "  make install    - Install dependencies using uv"
	@echo "  make dev        - Install dev dependencies"
	@echo "  make test       - Run tests"
	@echo "  make lint       - Run linting checks"
	@echo "  make format     - Format code"
	@echo "  make clean      - Clean cache files"
	@echo "  make run        - Run the development server"

install:
	uv sync

dev:
	uv sync --all-extras

test:
	uv run pytest

lint:
	uv run ruff check .
	uv run mypy src/app

format:
	uv run ruff format .
	uv run ruff check --fix .

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

run:
	cd src && uv run python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
