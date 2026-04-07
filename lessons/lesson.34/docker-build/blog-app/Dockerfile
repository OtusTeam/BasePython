FROM python:3.14.3-slim-trixie

ENV PYTHONUNBUFFERED=1

COPY --from=ghcr.io/astral-sh/uv:0.9.28 /uv /bin/

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1
# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy
# Omit development dependencies
ENV UV_NO_DEV=1
# Assert that the `uv.lock` will remain unchanged
ENV UV_LOCKED=1

WORKDIR /app

# скопировать конфиг зависимостей
COPY pyproject.toml uv.lock ./
# ставим зависимости
RUN uv sync --no-install-project
ENV PATH="/app/.venv/bin:$PATH"

# копируем entrypoint
COPY docker-build/blog-app/entrypoint.sh /etc/entrypoint.sh
RUN chmod +x /etc/entrypoint.sh

# копируем всё приложение
COPY blog-app ./

ENTRYPOINT ["/etc/entrypoint.sh"]
