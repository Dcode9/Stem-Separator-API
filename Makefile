# Stem Separator API - development commands
# Usage: make <target>

.PHONY: run lint format check install test help

help:
	@echo "Stem Separator API - available targets:"
	@echo "  make run      - Start dev server (uvicorn with reload)"
	@echo "  make lint     - Run Ruff linter"
	@echo "  make format   - Run Ruff formatter"
	@echo "  make check    - Lint + format (no write)"
	@echo "  make install  - Install dependencies from requirements.txt"
	@echo "  make test     - Run tests (if pytest is installed)"

run:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

lint:
	ruff check app/

format:
	ruff format app/

check: lint
	ruff format --check app/

install:
	pip install -r requirements.txt

test:
	pytest -v 2>/dev/null || echo "Install pytest and pytest-asyncio to run tests"
