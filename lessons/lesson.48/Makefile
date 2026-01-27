lint:
	poetry run pylint $(git ls-files '*.py')

test:
	poetry run pytest

coverage:
	poetry run pytest -s --cov --cov-report html --cov-fail-under 86
