FROM python:3.13.9-slim

WORKDIR /var/app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1
# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy
# Ensure installed tools can be executed out of the box
ENV UV_TOOL_BIN_DIR=/usr/local/bin

COPY --from=ghcr.io/astral-sh/uv:0.9.5 /uv /uvx /bin/

COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-install-project --no-dev

ENV PATH="/var/app/.venv/bin:$PATH"

COPY fastapi-app ./

CMD ["fastapi", "dev", "--host", "0.0.0.0"]
