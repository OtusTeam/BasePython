FROM python:3.13-bookworm

WORKDIR /var/app

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN pip install --upgrade pip "uv==0.6.14"

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-dev

ENV PATH="/var/app/.venv/bin:$PATH"

COPY ./magazine-app ./

RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]

#CMD ["gunicorn", "app:app", "--workers", "2", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8080"]
