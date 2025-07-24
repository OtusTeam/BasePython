from python:3.12

RUN apt-get update

COPY ./pyproject.toml ./pyproject.toml
COPY ./poetry.lock ./poetry.lock

RUN pip3 install --upgrade pip && pip3 install poetry && poetry install --no-root

COPY ./ ./