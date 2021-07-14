FROM python:3.9.6-buster

WORKDIR /app

RUN pip install poetry

RUN poetry config virtualenvs.create false

COPY ./web-app/pyproject.toml .
COPY ./web-app/poetry.lock .

RUN poetry install

COPY web-app ./

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host=0.0.0.0"]
