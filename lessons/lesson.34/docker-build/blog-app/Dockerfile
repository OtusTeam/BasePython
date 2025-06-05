FROM python:3.13.4-bookworm


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1
# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy


WORKDIR /var/app

RUN pip install --upgrade pip "uv==0.6.3"

COPY pyproject.toml uv.lock ./

RUN uv sync --locked --no-dev

ENV PATH="/var/app/.venv/bin:$PATH"

COPY blog-app .

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
