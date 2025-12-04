FROM python:3.13.9-slim

COPY --from=ghcr.io/astral-sh/uv:0.9.5 /uv /uvx /bin/

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1
# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy
# Ensure installed tools can be executed out of the box
ENV UV_TOOL_BIN_DIR=/usr/local/bin

WORKDIR /var/app

COPY pyproject.toml uv.lock ./

RUN uv sync --locked --no-install-project --no-dev

COPY docker-build/app/entrypoint.sh /etc/entrypoint.sh
RUN chmod +x /etc/entrypoint.sh

COPY blog-app ./

# Place executables in the environment at the front of the path
ENV PATH="/var/app/.venv/bin:$PATH"

ENTRYPOINT ["/etc/entrypoint.sh"]

CMD ["fastapi", "run", "--host", "0.0.0.0", "--port", "8000"]
