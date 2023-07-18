FROM python:3.11.4-slim-bookworm

WORKDIR /app

RUN pip install --upgrade pip setuptools "poetry==1.5.1"
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./
RUN poetry install --only main

COPY . .

CMD uvicorn main:app --host 0.0.0.0 --port 8000
