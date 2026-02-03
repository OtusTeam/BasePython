from python:3.13

RUN apt-get update

COPY ./poetry.lock ./poetry.lock
COPY ./pyproject.toml ./pyproject.toml

RUN pip3 install --upgrade pip
RUN pip3 install poetry
RUN poetry install
RUN pip3 install gunicorn

COPY ./ ./