FROM python:3.14-slim-trixie
COPY --from=ghcr.io/astral-sh/uv:0.12.21 /uv /uvx /bin/

# Setup a non-root user
RUN groupadd --system --gid 999 nonroot \
 && useradd --system --gid 999 --uid 999 --create-home nonroot

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

# Enable bytecode compilation after installation
ENV UV_COMPILE_BYTECODE=1
# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy
# Disable development dependencies
ENV UV_NO_DEV=1
# Assert dependencies from lock file remain unchanged
ENV UV_LOCKED=1
# Install the project's dependencies but not the project itself
ENV UV_NO_INSTALL_PROJECT=1

# Ensure installed tools can be executed out of the box
ENV UV_TOOL_BIN_DIR=/usr/local/bin


WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync

ENV PATH="/app/.venv/bin:$PATH"

COPY docker-build/app/entrypoint.sh /etc/entrypoint.sh
RUN chmod +x /etc/entrypoint.sh

COPY blog-app ./

# Use the non-root user to run our application
USER nonroot

ENTRYPOINT ["/etc/entrypoint.sh"]
