FROM python:3.12.4-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /var/app

RUN pip install --upgrade pip setuptools wheel "poetry==1.8.3"
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY fastapi-app ./

#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
CMD gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --access-logfile '-' --bind 0.0.0.0:8000

EXPOSE 8000
