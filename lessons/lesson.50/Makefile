test:
	poetry run pytest

server:
	python manage.py runserver

lint:
	pylint $(git ls-files '*.py')

coverage:
	pytest -s --cov --cov-report html --cov-fail-under 86
