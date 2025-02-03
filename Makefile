install:
	uv sync

gendiff:
	uv run gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml

lint:
	poetry run flake8 gendiff

selfcheck:
	uv check

check: selfcheck test lint

build:
	uv build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl