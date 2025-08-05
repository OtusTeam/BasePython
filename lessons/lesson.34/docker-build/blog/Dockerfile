FROM python:3.13-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --upgrade pip "uv==0.8.4"

COPY pyproject.toml uv.lock ./

RUN uv sync --locked

ENV PATH="/app/.venv/bin:$PATH"

COPY docker-build/blog/entrypoint.sh /etc/entrypoint.sh

RUN chmod +x /etc/entrypoint.sh

COPY blog-application .

ENTRYPOINT ["/etc/entrypoint.sh"]
