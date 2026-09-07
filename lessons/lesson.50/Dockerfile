FROM python:3.14

COPY ./poetry.lock ./poetry.lock
COPY ./pyproject.toml ./pyproject.toml

RUN pip3 install --upgrade pip && pip3 install poetry && poetry install

COPY ./ ./