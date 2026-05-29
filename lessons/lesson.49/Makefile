pylint:
	pylint $(shell git ls-files '*.py')

test:
	pytest

coverage:
	pytest --cov --cov-report html --cov-fail-under 85