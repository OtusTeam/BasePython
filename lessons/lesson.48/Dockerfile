FROM tiangolo/uwsgi-nginx-flask:python3.12

RUN pip install --upgrade pip "poetry==1.8.3" \
    && poetry config virtualenvs.create false --local

COPY ./prestart.sh ./prestart.sh

COPY poetry.lock pyproject.toml ./

RUN poetry install

COPY ./ ./
