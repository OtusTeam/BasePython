FROM tiangolo/uwsgi-nginx-flask:python3.11

RUN pip install --upgrade pip "poetry==1.8.3"
RUN poetry config virtualenvs.create false --local

COPY poetry.lock pyproject.toml ./

RUN poetry install

COPY ./prestart.sh ./prestart.sh

COPY ./app/ ./
