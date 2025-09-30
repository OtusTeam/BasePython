FROM python:3.13.7-trixie

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV UV_TOOL_BIN_DIR=/usr/local/bin

COPY --from=ghcr.io/astral-sh/uv:0.8.22 /uv /uvx /bin/

COPY pyproject.toml uv.lock ./

RUN uv sync --locked --no-install-project --no-dev

COPY blog-app ./
COPY docker-build/app/entrypoint.sh ./

ENV PATH="/app/.venv/bin:$PATH"

RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]

#CMD gunicorn --workers=1 --worker-class=uvicorn.workers.UvicornWorker --bind=localhost:8001 main:app

