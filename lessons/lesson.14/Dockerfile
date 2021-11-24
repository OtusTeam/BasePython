FROM python:3.9-buster

WORKDIR /var/app

#RUN pwd
#RUN ls -la

#COPY blog/requirements.txt ./requirements.txt
#RUN pip install -r requirements.txt

RUN pip install poetry==1.1.11

COPY blog/pyproject.toml blog/poetry.lock ./

RUN poetry config virtualenvs.create false

RUN poetry install

COPY blog .

#RUN pwd
#RUN ls -la

CMD uvicorn app:app --host=0.0.0.0
