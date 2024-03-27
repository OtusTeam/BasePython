FROM python:3.12.2-bookworm

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --upgrade pip poetry==1.8.2

RUN poetry config virtualenvs.create false --local
COPY pyproject.toml poetry.lock ./
RUN poetry install --only main

COPY fastapi-mini-app ./

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
