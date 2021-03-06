FROM python:3.9-buster

WORKDIR /var/app

RUN pip install poetry
RUN poetry --help
RUN poetry config virtualenvs.create false

COPY my-shop/pyproject.toml my-shop/poetry.lock ./

RUN poetry install --no-interaction --no-ansi

COPY my-shop/my_shop .

EXPOSE 5000

CMD python app.py
