FROM tiangolo/uwsgi-nginx-flask:python3.11

RUN pip install --upgrade pip "poetry==1.5.1"
RUN poetry config virtualenvs.create false --local

COPY poetry.lock pyproject.toml ./

RUN poetry install --no-ansi --only main

COPY . /app
