FROM python:3.9-buster

WORKDIR /var/app

RUN pip install poetry
RUN poetry config virtualenvs.create false

#COPY my-shop/pyproject.toml my-shop/poetry.lock ./
COPY my-shop/pyproject.toml ./

RUN poetry install --no-interaction --no-ansi

COPY my-shop .

RUN chmod +x entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["bash", "./entrypoint.sh"]
