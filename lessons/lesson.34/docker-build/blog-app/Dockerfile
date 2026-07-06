FROM python:3.14.6-slim-trixie

ENV PYTHONUNBUFFERED=1

COPY --from=ghcr.io/astral-sh/uv:0.11.7 /uv /bin/

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1
# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy
# Omit development dependencies
ENV UV_NO_DEV=1
# Assert that the `uv.lock` will remain unchanged
ENV UV_LOCKED=1

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --no-install-project

ENV PATH="/app/.venv/bin:$PATH"

COPY docker-build/blog-app/entrypoint.sh /etc/entrypoint.sh
RUN chmod +x /etc/entrypoint.sh

COPY blog-app ./

ENTRYPOINT ["/etc/entrypoint.sh"]
