FROM python:3.12-bookworm
#FROM python:3.12-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /var/app

RUN pip install --upgrade pip "poetry==1.8.4"

RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install --only main

COPY fastapi-app ./

RUN chmod +x prestart.sh

EXPOSE 8000

ENTRYPOINT ["./prestart.sh"]

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
