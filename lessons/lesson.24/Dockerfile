FROM python:3.11.7-bookworm

WORKDIR /app

RUN pip install "poetry==1.7.1"
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

COPY fastapi-greet-app ./

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]

EXPOSE 8000
